FROM python:3.9-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENV DATABASE_URL default

COPY . .
RUN pytest --cov --cov-report=html:template

CMD ["gunicorn","--reload", "wsgi:app", "--bind", "0.0.0.0:3008", "--log-level", "debug"]
