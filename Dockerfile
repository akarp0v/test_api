FROM python:3.8.6-slim

WORKDIR /test-api

COPY gorest gorest/

COPY test_api.py requirements.txt ./

RUN mkdir allure_reports

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update \
    && apt-get install --yes wget \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    # TODO: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=863199
    && mkdir -p /usr/share/man/man1 \
    # Download and install allure
    && wget https://github.com/allure-framework/allure2/releases/download/2.13.8/allure_2.13.8-1_all.deb \
    # Ignore dpkg error
    && dpkg -i allure_2.13.8-1_all.deb || true \
    && apt-get install -f --yes \
    && rm allure_2.13.8-1_all.deb \
    && rm -rf /var/lib/apt/lists/*

COPY ./entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]

CMD allure serve /test-api/allure_reports/ --port 38077
