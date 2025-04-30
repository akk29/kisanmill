# KisanMill

Hackathon Project | World Food India Hackathon 2017 | New Delhi , India

## Dependencies

[![Python](https://img.shields.io/badge/python-2.7.16-blue.svg?style=flat-square)](https://www.python.org/downloads/release/python-2716/)
[![Django Web Framework](https://img.shields.io/badge/Django-1.11.10-blue.svg?style=flat-square)](https://pypi.org/project/Django/1.11.10/)

---

### 1. Steps for setting project

```
# download source code
git clone https://github.com/akk29/kisanmill

# go inside directory
cd kisanmill

# path to python 2.7.16, setting up virtual environment
python.exe -m pip install --trusted-host pypi.python.org virtualenv
python -m virtualenv .venv
.venv\Scripts\activate # windows
source .venv/bin/activate # linux

# install requirements
pip install -r requirements.txt

# run development server locally
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8080
```

### 2. Steps for running project via docker

Pull publicly hosted image from docker repository & run directly on your system

```
docker run -d -p 8080:8000 --name kisanmill akk29/public:kisanmill
```

## Demo : [http://127.0.0.1:8080](http://127.0.0.1:8080) in your browser


[Documentation](docs.md)