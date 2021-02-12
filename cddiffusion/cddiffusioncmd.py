#!/usr/bin/env python

import os
import sys
import argparse
import traceback
import uuid
import json
from contextlib import redirect_stdout

import ndex2
import networkheatdiffusion


class Formatter(argparse.ArgumentDefaultsHelpFormatter,
                argparse.RawDescriptionHelpFormatter):
    pass


def _parse_arguments(desc, args):
    """
    Parses command line arguments
    :param desc:
    :param args:
    :return:
    """
    parser = argparse.ArgumentParser(description=desc,
                                     formatter_class=Formatter)
    parser.add_argument('input',
                        help='CX file')
    parser.add_argument('--input_attribute_name', default='diffusion_input',
                        help='The key diffusion will use to search for '
                             'heats in the node attributes')
    parser.add_argument('--output_attribute_name', default='diffusion_output',
                        help='Will be the prefix of the _rank and _heat '
                             'attributes created by diffusion')
    parser.add_argument('--normalize_laplacian', action='store_true',
                        help='If Set, will create a normalized laplacian '
                             'matrix for diffusion')
    parser.add_argument('--time', default=0.1, type=float,
                        help='The upper bound on the exponential '
                             'multiplication performed by diffusion')
    return parser.parse_args(args)


def run_diffusion(theargs, out_stream=sys.stdout,
                  err_stream=sys.stderr):
    """
    Runs diffusion and converts
    output to CDAPS compatible format that is output to
    standard out.

    :param theargs: Holds attributes from argparse
    :type theargs: `:py:class:`argparse.Namespace`
    :param out_stream: stream for standard output
    :type out_stream: file like object
    :param err_stream: stream for standard error output
    :type err_stream: file like object
    :return: 0 upon success otherwise error
    :rtype: int
    """

    if theargs.input is None or not os.path.isfile(theargs.input):
        err_stream.write(str(theargs.input) + ' is not a file')
        return 3

    if os.path.getsize(theargs.input) == 0:
        err_stream.write(str(theargs.input) + ' is an empty file')
        return 4

    try:
        with redirect_stdout(sys.stderr):
            net = ndex2.create_nice_cx_from_file(theargs.input)
            diffuser = networkheatdiffusion.HeatDiffusion()
            resnet = diffuser.run_diffusion(net, time_param=theargs.time,
                                            normalize_laplacian=
                                            theargs.normalize_laplacian,
                                            input_col_name=
                                            theargs.input_attribute_name,
                                            output_prefix=
                                            theargs.output_attribute_name,
                                            via_service=False)
            # write network as CX to output stream
            finalres = {}
            finalres['data'] = resnet.to_cx()
            finalres['errors'] = []
            json.dump(finalres, out_stream)
        return 0
    except networkheatdiffusion.HeatDiffusionError as he:
        err_stream.write(str(he))
        return 5
    finally:
        err_stream.flush()
        out_stream.flush()


def main(args):
    """
    Main entry point for program
    :param args: command line arguments usually :py:const:`sys.argv`
    :return: 0 for success otherwise failure
    :rtype: int
    """
    desc = """
    Runs Diffusion on command line, sending output to standard
    out in new 
    """
    theargs = _parse_arguments(desc, args[1:])
    try:
        return run_diffusion(theargs, sys.stdout, sys.stderr)
    except Exception as e:
        sys.stderr.write('\n\nCaught exception: ' + str(e))
        traceback.print_exc()
        return 2


if __name__ == '__main__':  # pragma: no cover
    sys.exit(main(sys.argv))
