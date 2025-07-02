#!/bin/bash
set -e

DIR_PATH=$(dirname ${BASH_SOURCE:-$0})

docker compose -f $DIR_PATH/docker-compose.yml --progress plain up -d --remove-orphans --quiet-pull
