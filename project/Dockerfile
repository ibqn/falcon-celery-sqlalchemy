# base image
FROM python:3.6-alpine

# set working directory
WORKDIR /srv

# add requirements
COPY ./requirements.txt /srv/requirements.txt

# install requirements
RUN apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    python3 -m pip install --no-cache-dir --upgrade pip setuptools && \
    python3 -m pip install --no-cache-dir --upgrade --requirement requirements.txt && \
    apk --purge del .build-deps
