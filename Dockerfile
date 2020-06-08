FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /delivery_api
WORKDIR /delivery_api

RUN apk update && apk add --no-cache postgresql-dev gcc musl-dev bash

RUN pip install --no-cache-dir --upgrade pip pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile

COPY run_web.sh ./
RUN chmod +x run_web.sh

ENTRYPOINT ["bash", "./run_web.sh"]

COPY . /delivery_api/
EXPOSE 8000