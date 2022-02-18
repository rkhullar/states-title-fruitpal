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

2. install dependencies for `backend` and `library`
```shell
cd path/to/component
. venv/bin/activate
pip install -U pip setuptools
pip install pipenv
pipenv install --dev
```

##### running fastapi
3. prepare terminal
```shell
cd path/to/backend
. venv/bin/activate
cd fastapi
```

4. create sqlite database
```shell
alembic upgrade head
```

5. start fastapi service
```shell
python main.py
```

6. explore openapi docs
- http://localhost:8000/docs

##### running client
7. prepare terminal
```shell
cd path/to/library
. venv/bin/activate
```

8. package library
```shell
python setup.py bdist_wheel
rm -rf build *.egg-info
```

The first command creates three directories: `build` `dist` and `fruitpal.egg-info`. We only need `dist` since it
contains the wheel file, which we'll install in the `example` virtual environment.

9. install library
```shell
cd path/to/example
. venv/bin/activate
pip install ../library/dist/fruitpal-*.whl
```

10. configure environment
```shell
export FRUITPAL_BASE_URL='http://localhost:8000/api/v1'
```

11. import vendors
```shell
fruitpal import-vendors vendors.json
fruitpal read-vendors
```

12. show estimate
```shell
fruitpal estimate --help
fruitpal estimate mango 53 403
```

### Future Ideas

#### Testing
The project structure for both the backend and library components does allow for testing. Especially since the main
fastapi service is implemented with the factory pattern. See the following for examples in other projects:
- [rkhullar/hello-fastapi](https://github.com/rkhullar/hello-fastapi/tree/0de5ea2fb764aa75df7a8e4a446db35ea4ad8bff/fastapi/api/tests)
- [rkhullar/aws-sso](https://github.com/rkhullar/aws-sso/tree/14e019187e411bdeee77152310b09d250ec90555/aws_sso/tests)

#### Code Generation
Since the fastapi service has openapi documentation, it should be possible to generate modern libraries for multiple
programming languages.

#### Database
If this project were to be deployed, we obviously wouldn't use SQLite. If hosting on AWS, using Amazon Aurora would be
ideal, since it's compatible with both MySQL and PostgreSQL and has autoscaling.

Alternatively, the database and orm can be swapped with MongoDB Atlas with Mongoengine. Two advantages in doing so are
as follows:
- You can manage documents directly in the browser at MongoDB Cloud.
- Database migrations become unnecessary.

#### Asynchronicity
The client library calls the fastapi service synchronously. It would be ideal for the library to operate depending on
the caller, but it would be challenging to implement that while keeping the code DRY and relatively simple.

Perhaps one way would be to implement something similar to `httpx.AsyncClient`. Basically the library could provide a
context manager that wraps that somehow converts the sync requests to async.
- https://www.python-httpx.org/async

#### Random Notes

##### Updating the Data Model
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
