# Falcon and uWSGI
Falcon is faster than [flask](/pallets/flask), uWSGi [uWSGI](/unbit/uwsgi) is faster than [Gunicorn](/benoitc/gunicorn).
Test based on [pceuropa/testing-rest-api](/pceuropa/testing-rest-api)

DIRECTORY STRUCTURE
-------------------
      requirements.txt      pythons requirements packages 
      main.py               falcon app
      uwsgi.ini             contains config file needed to run app by uwsgi
      tests.py              tests based on pytest

REQUIREMENTS
------------
- Python 3+
- pytest # to tests

INSTALATION
----------
```
virtualenv -p python3 venv && source venv/bin/activate
pip3 install -r requirements.txt
```

CONFIGURATION
----------
Configuration is in uwsgi.ini. Only Set proper patch and ready to run.

RUN
----------
1. Without uwsgi
```
python3 main.py
```

2. With uwsgi but by command. Please run this command on path of application
```bash
uwsgi --http :8000 --wsgi-file main.py --callable app -H $(pwd)/venv/
```

3. With uwsgi with help ini file. Good way to setup systemd
```bash
uwsgi uwsgi.ini
```


Tests
---------------
```
mytest test.py -v
```
