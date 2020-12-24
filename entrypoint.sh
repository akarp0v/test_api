#!/bin/bash

pytest -v --alluredir=/test-api/allure_reports

exec "$@"