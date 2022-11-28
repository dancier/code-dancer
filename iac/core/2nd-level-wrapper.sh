#!/bin/bash

if [ -z ${RUN_ENV} ];
  then 
    echo "You have to provide the path to the docker-compose file as an environment-variable RUN_ENV"
    exit 1;
fi

cd ${RUN_ENV}

function deploy() {
    export SERVICE=$1
    VAR_NAME=${SERVICE^^}_TAG
    VAR_NAME=${VAR_NAME//-/_}
    export ${VAR_NAME}=${2}
    echo "Using Tag var: ${VAR_NAME}"
    echo "With Value: ${${VAR_NAME}}"
    echo "Pulling ${SERVICE} with TAG: $2"
    docker-compose pull ${SERVICE}
    docker-compose up -d --no-deps ${SERVICE}
}

case $1 in
    help)
        echo "Usage: 2nd-level-wrapper.sh command command_options..."
        echo "Where command can be deploy"
        echo "Deploy options are: servicename and tag"
    ;;
    deploy)
        if (( $# == 3 ))   ;
            then
                deploy $2 $3
            else
                echo "the deploy commands needs two parameters"
                
        fi        
    ;;
    *)
        echo "Unkown command... $1"

esac