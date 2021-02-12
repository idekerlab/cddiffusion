FROM continuumio/miniconda3

RUN conda install -y -c conda-forge scipy
RUN conda install -y -c conda-forge networkx

RUN mkdir /tmp/networkheatdiffusion \
         && cd /tmp/networkheatdiffusion \
         && git clone --depth 1 https://github.com/idekerlab/networkheatdiffusion \
         && cd networkheatdiffusion \
         && /opt/conda/bin/python setup.py bdist_wheel \
         && /opt/conda/bin/pip install dist/networkheatdiffusion*whl \
         && cd /tmp \
         && rm -rf /tmp/networkheatdiffusion

RUN mkdir /tmp/cddiffusion
COPY dist/*.whl /tmp/cddiffusion

RUN /opt/conda/bin/pip install /tmp/cddiffusion/cddiffusion*whl

RUN rm -rf /tmp/cddiffusion

RUN /opt/conda/bin/pip uninstall enum34 -y

ENTRYPOINT ["/opt/conda/bin/cddiffusioncmd.py"]
CMD ["--help"]
