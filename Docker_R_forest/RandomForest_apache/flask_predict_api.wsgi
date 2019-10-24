#! /usr/bin/python

import sys
sys.path.insert(0, "/var/www/flask_predict_api")
sys.path.insert(0,'/opt/conda/lib/python3.7/site-packages')
sys.path.insert(0, "/opt/conda/bin/python3")

import os
os.environ['PYTHONPATH'] = '/opt/conda/bin/python3'

from flask_usage import app as application