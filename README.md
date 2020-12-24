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
Pytest version:
`docker run sen10rqa/api-tests`

Allure version:
`docker run -it -p 38077:38077 sen10rqa/api-tests-allure`

[Pytest version link](https://hub.docker.com/repository/docker/sen10rqa/api-tests)

[Allure version link](https://hub.docker.com/repository/docker/sen10rqa/api-tests-allure)

**Build Docker container instruction:**

1. clone git repository: `git clone https://github.com/akarp0v/test_api.git`

2. build image:
`docker build -t api-tests-allure .`

3. run:
`docker run -it -p 38077:38077 api-tests-allure`

4. [check Allure dashboard](http://localhost:38077/index.html)
