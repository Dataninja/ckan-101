FROM python:3.9

RUN mkdir -p /opt/app
WORKDIR /opt/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "gunicorn" ]
CMD [ "--bind", "0.0.0.0:5000", "wsgi:app" ]
