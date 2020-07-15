FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update -y
RUN apt-get install gettext -y

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/