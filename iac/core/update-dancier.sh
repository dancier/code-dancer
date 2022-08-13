#!/bin/bash

cd /run-env

./db-dump.sh
docker-compose pull
docker-compose down
docker-compose up --build -d