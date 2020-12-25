#!/bin/bash

pytest -v --alluredir=/test-api/allure_reports

echo "Allure dashboard link: http://localhost:38077/"

exec "$@"
