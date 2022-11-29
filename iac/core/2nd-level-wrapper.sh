#!/bin/bash

if [ -z ${RUN_ENV} ];
  then 
    echo "You have to provide the path to the docker-compose file as an environment-variable RUN_ENV"
    exit 1;
fi

cd ${RUN_ENV}

function check_service() {
    CHOOSEN_SERVICE=$1
    case $CHOOSEN_SERVICE in 
        dancer|chat-dancer|show-dancer|recommendation|kikeriki)
        ;;
        *)
        echo "Unsported service $CHOOSEN_SERVICE"
        exit 1
    esac

}

function deploy() {
    export SERVICE=$1
    check_service $SERVICE
    VAR_NAME=${SERVICE^^}_TAG
    VAR_NAME=${VAR_NAME//-/_}
    export ${VAR_NAME}=${2}
    echo "Using Tag var: ${VAR_NAME}"
    echo "With Value: ${!VAR_NAME}"
    echo "Pulling ${SERVICE} with TAG: $2"
    docker-compose pull ${SERVICE}
    docker-compose up -d --build --no-deps ${SERVICE}
}

case $1 in
    deploy)
        if (( $# == 3 ))   ;
            then
                deploy $2 $3
            else
                echo "the deploy commands needs two parameters"
                
        fi
    ;;
    up)
        docker-compose up -d $2
    ;;
    stop)
        docker-compose stop $2 
    ;;
    ps)
        docker-compose ps
    ;;
    stats)
        docker stats --no-stream
    ;;
    *|help)
        echo "Usage: 2nd-level-wrapper.sh command command_options..."
        echo "Where command can be deploy, up, stop, ps, stats"
        echo "Deploy options are: servicename and tag"

esac