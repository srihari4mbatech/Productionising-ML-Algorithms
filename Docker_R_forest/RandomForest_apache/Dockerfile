FROM continuumio/miniconda3
MAINTAINER Srihari
EXPOSE 8000
RUN apt-get update && apt-get install -y apache2 apache2-dev make \
&& apt-get clean \
&& apt-get autoremove \
&& rm -rf /var/lib/apt/lists/*
COPY . /var/www/flask_predict_api/
RUN make /var/www/flask_predict_api/ \
    && pip install -r /var/www/flask_predict_api/requirements.txt
RUN /opt/conda/bin/mod_wsgi-express install-module
RUN mod_wsgi-express setup-server flask_predict_api.wsgi --port=8000 \
    --user www-data --group www-data \
    --server-root=/etc/mod_wsgi-express-80
CMD /etc/mod_wsgi-express-80/apachectl start -D FOREGROUND