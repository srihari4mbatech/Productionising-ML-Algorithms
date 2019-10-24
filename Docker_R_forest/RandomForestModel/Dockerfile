FROM continuumio/miniconda3
MAINTAINER srihari
ENV http_proxy http://proxy-iind.intel.com:911
ENV https_proxy https://proxy-iind.intel.com:911
EXPOSE 5000
COPY . /RandomForestModel
RUN apt-get install make
RUN make /RandomForestModel && conda create -y -n tempenv -c conda-forge --file /RandomForestModel/requirements.txt
ENV PATH /opt/conda/envs/tempenv/bin:$PATH
CMD /bin/bash -c "source activate tempenv && python3 /RandomForestModel/flask_usage.py"