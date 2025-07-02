#!/bin/bash
set -e

DIR_PATH=$(dirname ${BASH_SOURCE:-$0})

docker compose -f $DIR_PATH/docker-compose.yml --progress plain kill
docker compose -f $DIR_PATH/docker-compose.yml --progress plain rm -f