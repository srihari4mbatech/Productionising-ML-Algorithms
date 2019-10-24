sudo docker pull python:3.6-alpine

## Docker file content for python:3
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./your-daemon-or-script.py" ]

# For single file its convenient to run docker container from single line of command as stated below
docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python your-daemon-or-script.py

docker run -i -t python:3.6-slim /bin/bash

docker run -i -t python_custom:3.6-slim /bin/bash

docker run -i -t continuumio/miniconda3 /bin/bash
docker run -i -t -p 8888:8888 continuumio/miniconda3 /bin/bash -c "/opt/conda/bin/conda install jupyter -y --quiet && mkdir /opt/notebooks && /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser --allow-root"


sudo docker run -it --rm --name sample -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3.6-slim python sample.py
sudo docker run -it --rm --name sample -v "$PWD":/usr/src/myapp -w /usr/src/myapp python_custom:3.6-slim python sample.py

sudo docker tag [SOURCE_IMAGE] [HOSTNAME]/[PROJECT-ID]/[IMAGE]

sudo docker push [HOSTNAME]/[PROJECT-ID]/[IMAGE]

Hostname -> gcr.io
PROJECT-id -> prismatic-will-254121
image->python_custom
tag->0.0.1

sudo docker tag python_custom:3.6-slim gcr.io/prismatic-will-254121/python_custom:0.0.1
sudo docker push gcr.io/prismatic-will-254121/python_custom:0.0.1
gcloud docker -- push gcr.io/prismatic-will-254121/python_custom:0.0.1

gcloud components install docker-credential-gcr