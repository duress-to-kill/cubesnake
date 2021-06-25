FROM python:3.8-buster
COPY . /app
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends
RUN python3 -m pip install pipenv
RUN pipenv install --deploy --system
EXPOSE 8080
#CMD pipenv run gunicorn server:app
CMD [ \
    "gunicorn", \
    "--bind=0.0.0.0:8080", \
    "--workers=2", \
    "server:app" \
]
