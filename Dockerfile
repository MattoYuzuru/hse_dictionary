FROM python:3.12.4-alpine3.20

RUN apk add mariadb-dev build-base

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY site_settings .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "site_settings.wsgi"]
#CMD ["python", "manage.py", "runserver"]
