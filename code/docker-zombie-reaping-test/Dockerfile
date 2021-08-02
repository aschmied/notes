FROM debian:buster

RUN apt-get update && \
  apt-get install -y \
    curl \
    g++ \
    procps

COPY entrypoint.sh /
COPY test-zombie.c /
RUN gcc -std=c99 test-zombie.c -o test-zombie

#ENTRYPOINT ["/usr/bin/tini", "--", "/entrypoint.sh"]
ENTRYPOINT ["/entrypoint.sh"]
