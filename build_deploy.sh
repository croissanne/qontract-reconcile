#!/bin/bash

# We want jenkins to fail hard
set -e

DOCKER_CONF="$PWD/.docker"
mkdir -p "$DOCKER_CONF"
docker --config="$DOCKER_CONF" login -u="$QUAY_USER" -p="$QUAY_TOKEN" quay.io

# build images
make test build push

make pypi-release
