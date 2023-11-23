FROM python:3.9-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENV USERS_URL default
ENV DATABASE_URL default
ENV GCP_JSON default
ENV COMPANY_URI default
ENV EMPLOYEE_URI default

COPY . .
#RUN pytest --cov --cov-report=html:template

CMD ["gunicorn","--reload", "wsgi:app", "--bind", "0.0.0.0:3007", "--log-level", "debug"]
