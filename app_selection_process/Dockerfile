FROM python:3.9-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENV USERS_URL default
ENV DATABASE_URL default
ENV GCP_JSON default
ENV PROJECT_URI default
ENV CONTRACT_URI default
ENV PERFORMANCE_URI default

COPY . .

CMD ["gunicorn","--reload", "wsgi:app", "--bind", "0.0.0.0:3010", "--log-level", "debug"]
