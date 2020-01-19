#!/bin/bash

echo "Starting the dancer app."
echo "It will start the lastes docker image: dancier/dancer:1.0"
echo "It will kill the currently running one."
echo "Expect a downtime"

TARGET=mumble.frubumi.de

ssh root@$TARGET << EOF
    docker stop dancer
    docker rm dancer
    docker pull dancier/dancer:1.0
    docker run --name dancer  -d -p 8080:8080 dancier/dancer:1.0
EOF
