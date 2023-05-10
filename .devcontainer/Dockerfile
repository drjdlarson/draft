FROM debian:bullseye-slim

ARG USER_UID=1000
ARG USER_GID=1000

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        openssh-client \
        libssl-dev \
        python3-pip \
        python-is-python3 \
        git \
    && rm -rf /var/lib/apt/lists/*

