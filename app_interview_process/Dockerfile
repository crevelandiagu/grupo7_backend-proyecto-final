FROM python:3.9

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENV USER_URL=localhost

COPY . .

CMD ["gunicorn","--reload", "wsgi:app", "--bind", "0.0.0.0:3010", "--log-level", "debug"]
