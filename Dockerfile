FROM python:3.8-buster
COPY . /app
RUN python3 -m pip install pipenv
RUN pipenv install
CMD gunicorn server:app
