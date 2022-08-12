#!/bin/bash

cd /run-env
docker-compose pull
docker-compose down
docker-compose up -d