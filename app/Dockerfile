FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

COPY requirements.txt /code/

COPY . /code/

WORKDIR /code

RUN pip install -U pip

RUN pip install -r requirements.txt \
    && python -m nltk.downloader punkt