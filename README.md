# KisanMill

KisanMill is a B2C & C2C platform for Agriculture Sector to eliminate the middleman & increase profits.

Hackathon Project | World Food India Hackathon 2017 | New Delhi, India

## Dependencies

[![Python](https://img.shields.io/badge/python-3.13.3-blue.svg?style=flat-square)](https://www.python.org/downloads/release/python-3133/)
[![Django Web Framework](https://img.shields.io/badge/Django-5.2-blue.svg?style=flat-square)](https://pypi.org/project/Django/5.2/)

---

### 1. Steps for setting project

```shell
# download source code
git clone https://github.com/akk29/kisanmill

# go inside directory
cd kisanmill

# setting up virtual environment
python -m virtualenv .venv
.venv\Scripts\activate # windows
source .venv/bin/activate # linux

# install requirements
pip install -r requirements.txt

# run development server locally
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

### 2. Steps for running project via docker

```shell
docker compose up
```

## Demo : [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser


[Documentation](docs.md)