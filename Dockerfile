# Dockerfile for python test api script

FROM python:3.8

WORKDIR /test-api

COPY gorest/gorest_api.py test_api.py users.py token requirements.txt ./

RUN pip install -r requirements.txt

CMD ["pytest", "-v"]
