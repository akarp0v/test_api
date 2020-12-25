#!/bin/bash

pytest -v --alluredir=/test-api/allure_reports

echo -e "\n\e[33mClick Allure dashboard link http://localhost:38077/ after Server started...\e[0m\n"

exec "$@"
