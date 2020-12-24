FROM python:3.8.6-slim

WORKDIR /test-api

COPY gorest gorest/

COPY test_api.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

RUN brew install allure

CMD ["pytest", "-v", "--alluredir=allure_reports/"]

CMD ["allure", "serve", "allure_reports/"]
