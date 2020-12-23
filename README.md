Python REST API test framework

REST API: https://gorest.co.in

run:
$ pytest -v

Test steps:
1. POST
2. PUT
3. PATCH
4. DELETE

Docker
---
run:
$ docker run sen10rqa/api-tests

repository: 
https://hub.docker.com/repository/docker/sen10rqa/api-tests

build image locally:
$ docker build -t api-tests .

run locally:
$ docker run api-tests
