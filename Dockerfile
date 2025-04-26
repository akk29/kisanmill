FROM python:2
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
RUN [ "python", "manage.py", "collectstatic" ,"--no-input" ]
RUN [ "python", "manage.py", "makemigrations" ]
RUN [ "python", "manage.py", "migrate" ]
CMD ["gunicorn","--bind","0.0.0.0:8000","kisanmill.wsgi"]