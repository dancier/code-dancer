#!/bin/bash

cd /run-env

db-dump_chat_dancer.sh
db-dump_dancer.sh
db-dump_iam.sh
db-dump_recommendation.sh
docker compose pull
docker compose down
docker compose up --build -d