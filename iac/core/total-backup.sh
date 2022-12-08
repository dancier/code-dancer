#!/bin/bash

if [ -z ${RUN_ENV} ];
  then 
    echo "You have to provide the path to the docker-compose file as an environment-variable RUN_ENV"
    exit 1;
fi

cd ${RUN_ENV}

docker-compose down

docker-compose up -d iam-db
docker-compose up -d chat-dancer-db
docker-compose up -d dancer-db
docker-compose up -d recommendation-db