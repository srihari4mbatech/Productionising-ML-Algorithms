FROM continuumio/miniconda3
MAINTAINER Srihari
EXPOSE 5000
RUN apt-get update && apt-get install \
    && apt-get clean \
    && apt-get autoremove 
COPY . /RandomForestModel/
RUN make /RandomForestModel/ \
    && pip install -r /RandomForestModel/requirements.txt
CMD python /RandomForestModel/flask_usage.py

