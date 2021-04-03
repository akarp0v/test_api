## [REST API](https://gorest.co.in) test automation mini framework

> #### Python | Pytest | Allure | Docker

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies

```
pip install requirements.txt 
```

## Usage

Test steps:
1. POST request
2. PUT request
3. PATCH request
4. DELETE request

Run Pytest version

```
pytest -v
```

Run Allure version

```
pytest -v --alluredir=allure_reports
```

```
allure serve allure_reports
```


## Docker

Run Pytest version

```
docker run sen10rqa/api-tests
```

Run Allure version

```
docker run -it -p 38077:38077 sen10rqa/api-tests-allure
```

>[Allure dashboard link](http://localhost:38077/index.html)

**Docker Hub repository**

[Pytest version link](https://hub.docker.com/repository/docker/sen10rqa/api-tests)

[Allure version link](https://hub.docker.com/repository/docker/sen10rqa/api-tests-allure)

**Docker container build instruction**

1. Clone git repository `git clone https://github.com/akarp0v/test_api.git`

2. Build image `docker build -t api-tests-allure .`

3. Run `docker run -it -p 38077:38077 api-tests-allure`

4. Click [Allure dashboard link](http://localhost:38077/index.html)

## License

[MIT](https://choosealicense.com/licenses/mit/)
