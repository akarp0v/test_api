Python [REST API](https://gorest.co.in) test framework

Test steps:
1. POST request
2. PUT request
3. PATCH request
4. DELETE request

Pytest
---

`pytest -v`

Allure
---

`pytest -v --alluredir=allure_reports/`

`allure serve allure_reports/`


Docker
---

`docker run sen10rqa/api-tests`

[Repository link](https://hub.docker.com/repository/docker/sen10rqa/api-tests)

**Build Docker container instruction:**

- clone git repository: `git clone https://github.com/akarp0v/test_api.git`

- build image:
`docker build -t api-tests .`

- run:
`docker run api-tests`
