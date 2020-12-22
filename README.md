Python REST API test framework

REST API: https://gorest.co.in

run:
$ pytest -v
---
Test #1
1. POST
2. GET
3. DELETE
4. GET

Test #2
1. POST
2. PUT
3. GET 
4. DELETE
5. GET

Docker
---
build image locally:
$ docker build -t api-tests .

run locally:
$ docker run api-tests

run docker hub image:
$ docker run sen10rqa/api-tests

https://hub.docker.com/repository/docker/sen10rqa/api-tests
