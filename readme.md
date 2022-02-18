## Fruitpal

### Project
This projects serves as an example for creating a restful api service with a corresponding client library and cli.
All three components are written with Python 3.10, and the framework for the backend is FastAPI. The backend stores
data in SQLite through SQLAlchemy, but in retrospect it would have been better to use MongoDB Atlas and Mongoengine.

The main feature of the problem statement is to provide traders the full cost of buying fruit from various countries.
Users provide three points of information to FruitPal as follows:
- commodity
- price per ton (dollars)
- trade volume (tons)

And receive the purchase cost report as a list with two points of information:
- country code
- purchase cost

For example, a trader who wants to know the full cost of buying 405 tons of mangos at $53 a ton could run the following:
```shell
fruitpal mango 53 405
```
```text
BR 22040.10
MX 21967.20
```

With this example there are two vendors in Brazil and Mexico that supply mangos. Each vendor has a variable overhead
for calculating the total cost, in order to account for market overhead like fees and taxes. The vendor data for this
example is shown in [`example/vendors.json`](example/vendors.json).

The formula for total purchase cost is as follows: Also, the results are sorted from highest to lowest.
```text
(price_per_ton + variable_overhead) * trade_volume => purchase_cost
```
```text
(53+1.42)*405 => $22,040.10
(53+1.24)*405 => $21,967.20
```

### Instructions  

#### Local Setup
1. create python virtual environments
```shell
asdf local python 3.10.2
python -m venv backend/venv
python -m venv library/venv
python -m venv example/venv
```

NOTE: This may be not be required, but it's good to run `deactivate` when switch between virtual environments.

1. install dependencies for `backend` and `library`
```shell
cd path/to/component
. venv/bin/activate
pip install -U pip setuptools
pip install pipenv
pipenv install --dev
```

##### running fastapi
1. prepare terminal
```shell
cd path/to/backend
. venv/bin/activate
cd fastapi
```

1. create sqlite database
```shell
alembic upgrade head
```

1. start fastapi service
```shell
python main.py
```

1. explore openapi docs
- http://localhost:8000/docs

##### running client
1. prepare terminal
```shell
cd path/to/library
. venv/bin/activate
```

1. package library
```shell
python setup.py bdist_wheel
rm -rf build *.egg-info
```

The first command creates three directories: `build` `dist` and `fruitpal.egg-info`. We only need `dist` since it
contains the wheel file, which we'll install in the `example` virtual environment.

1. install library
```shell
cd path/to/example
. venv/bin/activate
pip install ../library/dist/fruitpal-*.whl
```

1. configure environment
```shell
export FRUITPAL_BASE_URL='http://localhost:8000/api/v1'
```

1. import vendors
```shell
fruitpal import-vendors vendors.json
fruitpal read-vendors
```

1. show estimate
```shell
fruitpal estimate --help
fruitpal estimate mango 53 403
```

#### Random Notes

##### alembic
```shell
cd path/to/backend/fastapi
alembic revision --autogenerate -m 'first migration'
alembic upgrade head
```

#### Links
- https://fastapi.tiangolo.com/tutorial/sql-databases
- https://restfulapi.net/resource-naming
- https://github.com/jubins/Fruitpal
- https://ahmed-nafies.medium.com/fastapi-with-sqlalchemy-postgresql-and-alembic-and-of-course-docker-f2b7411ee396
