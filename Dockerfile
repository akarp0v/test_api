# Dockerfile for python test api script

FROM python:3.8

WORKDIR /test-api

COPY gorest gorest/

COPY test_api.py requirements.txt ./

RUN pip install -r requirements.txt

CMD ["pytest", "-v"]
