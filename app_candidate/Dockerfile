FROM python:3.9

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENV USERS_URL default
ENV DATABASE_URL postgresql://admin:-BcjB(IiHYp`6_=8@192.168.0.3:5432/candidates-bd
COPY . .

CMD ["gunicorn","--reload", "wsgi:app", "--bind", "0.0.0.0:3000", "--log-level", "debug"]
