#!/bin/bash

cd /run-env

./db_dump_chat_dancer.sh
./db_dump_dancer.sh
./db_dump_iam.sh
./db_dump_recommendation.sh
docker-compose pull
docker-compose down
docker-compose up --build -d