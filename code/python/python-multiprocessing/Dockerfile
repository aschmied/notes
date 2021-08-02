FROM nanometrics/python3:1.0.0

ENV PYTHONUNBUFFERED 1

# RUN apk add tini

COPY entrypoint.sh .
RUN chmod u+x entrypoint.sh

COPY main.py .

# ENTRYPOINT ["tini", "-v", "--", "./entrypoint.sh"]
ENTRYPOINT ["./entrypoint.sh"]
