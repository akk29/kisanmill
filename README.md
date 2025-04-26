# KisanMill

Hackathon Project | World Food India Hackathon 2017 | New Delhi , India

## Dependencies

[![Python](https://img.shields.io/badge/python-2.7.16-blue.svg?style=flat-square)](https://www.python.org/downloads/release/python-2716/)
[![Django Web Framework](https://img.shields.io/badge/Django-1.11.10-blue.svg?style=flat-square)](https://pypi.org/project/Django/1.11.10/)

---

### 1. Steps for setting project locally - via source code (Will take time)

```
# download source code
git clone https://github.com/akk29/kisanmill

# go inside directory
cd kisanmill

# path to python 2.7.16, setting up virtual environment
python.exe -m pip install --trusted-host pypi.python.org virtualenv
python -m virtualenv .venv
source .venv/bin/activate

# install requirements
pip install -r requirements.txt

# run development server locally
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8080
```

### 2. Steps for runing project locally - via Docker image (Easy & preferred - no dependencies installation)

Pull publicly hosted image from docker repository & run directly on your system

```
docker run -d -p 8080:8000 --name kisanmill babygame0ver/docker-repository:kisanmill
```

## Demo : [http://127.0.0.1:8080](http://127.0.0.1:8080) in your browser


[Documentation](docs.md)