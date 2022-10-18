FROM python:3.9-slim
#FROM python:3.9-alpine


RUN apk add --update --no-cache \
        tini \
        py-gunicorn \
        libxml2-dev \
        libxslt-dev \
        libffi-dev \
        openssl-dev \
        build-base \
        libpq \
        postgresql-dev

RUN pip install --upgrade pip

RUN mkdir -p /opt/datapusher && cd /opt/datapusher

COPY . .

RUN pip install -r requirements.txt && python setup.py develop

RUN pip install --upgrade gunicorn psycopg2 requests

ENV JOB_CONFIG='/opt/datapusher/src/datapusher/deployment/datapusher_settings.py'

ENTRYPOINT ["/sbin/tini", "--"]
CMD ["gunicorn", "-b 0.0.0.0:8800", "wsgi:app"]

EXPOSE 8800
