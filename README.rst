===================================================
Network Heat Diffusion
===================================================

This repository creates a `CDAPS <https://github.com/cytoscape/communitydetection-rest-server>`__ compatible Diffusion Docker image using Network Heat Diffusion
packaged from https://github.com/idekerlab/networkheatdiffusion

Dependencies
------------

* `Docker <https://www.docker.com/>`_
* `make <https://www.gnu.org/software/make/>`_ (to build)
* Python (to build)

Building
--------

.. code-block::

   git clone https://github.com/idekerlab/cddiffusion
   cd cddiffusion
   make dockerbuild

Run **make** command with no arguments to see other build/deploy options including creation of Docker image

.. code-block::

   make

Output:

.. code-block::

   clean                remove all build, test, coverage and Python artifacts
   clean-build          remove build artifacts
   clean-pyc            remove Python file artifacts
   clean-test           remove test and coverage artifacts
   lint                 check style with flake8
   test                 run tests quickly with the default Python
   test-all             run tests on every Python version with tox
   coverage             check code coverage quickly with the default Python
   docs                 generate Sphinx HTML documentation, including API docs
   servedocs            compile the docs watching for changes
   testrelease          package and upload a TEST release
   release              package and upload a release
   dist                 builds source and wheel package
   install              install the package to the active Python's site-packages
   dockerbuild          build docker image and store in local repository
   dockerpush           push image to dockerhub


Usage
-----

.. code-block::

   docker run -v coleslawndex/cddiffusion:0.0.1 -h


Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
