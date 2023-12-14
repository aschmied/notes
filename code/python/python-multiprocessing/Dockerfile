FROM python:3.10

ENV PYTHONUNBUFFERED 1

COPY entrypoint.sh .
RUN chmod u+x entrypoint.sh

COPY main.py .

ENTRYPOINT ["./entrypoint.sh"]
