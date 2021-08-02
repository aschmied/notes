# Based on Knative's helloworld-python example:
#     https://knative.dev/docs/serving/samples/hello-world/helloworld-python/
#
# Run locally from Docker Hub:
#     docker run --rm --detach --env PORT=8080 --publish 8080:8080 --name hello-world-webapp nanometrics/hello-world-webapp:latest
#
# Build with:
#     docker build -t nanometrics/hello-world-webapp:latest .
#
# Push to Docker Hub with:
#     docker push nanometrics/hello-world-webapp:latest

FROM python:3.7.5-slim-buster

RUN pip install --no-cache-dir \
    Flask \
    gunicorn

COPY app.py .

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
