FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD docker/django/requirements.txt /code/
RUN pip install -r requirements.txt