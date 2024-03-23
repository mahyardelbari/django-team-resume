# django team resume


## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/mahyardelbari/django-team-resume
$ cd django-team-resume
$ cd src
$ cd config


```

Create a virtual environment to install dependencies in and activate it:

### in linux
```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```
### in windows
```sh
$ pyhton -m venv venv
$ .\env\bin\activate
```
Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.
Once `pip` has finished downloading the dependencies:

- Makemigrations and migrate are used to create and migrate the database.

    ```sh
    (env)$ cd project
    (env)$ python manage.py makemigrations
    (env)$ python manage.py migrate
    ```
- And run the server:

  ```sh
  (env)$ python manage.py runserver
  ```

  And navigate to `http://127.0.0.1:8000/`.


## Tests

To run the tests, `cd` into the directory where `manage.py` is:

```sh
(env)$ python manage.py test 
```
