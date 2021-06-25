FROM python:3.8-buster
COPY . /app
WORKDIR /app
RUN python3 -m pip install pipenv
RUN pipenv install
CMD pipenv run gunicorn server:app
