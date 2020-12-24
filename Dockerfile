FROM python:3.8.6-slim

WORKDIR /test-api

COPY gorest gorest/

COPY test_api.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["pytest", "-v", "--alluredir=allure_reports/"]

CMD ["allure", "serve", "allure_reports/"]
