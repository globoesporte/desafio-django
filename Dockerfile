# use base python image with python 3
FROM python:3

# add requirements.txt to the image
ADD requirements.txt /app/requirements.txt

WORKDIR /app

# install python dependencies
RUN pip install -r requirements.txt

# create unprivileged user
RUN adduser --disabled-password --gecos '' myuser