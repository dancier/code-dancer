if [ -z ${RUN_ENV} ];
  then 
    echo "You have to provide the path to the docker-compose file as an environment-variable RUN_ENV"
    exit 1;
fi

cd ${RUN_ENV}

FILENAME=db_dump_recommendation_${NOW}.sql.gz
echo "Dumping into ${FILENAME}"
docker exec recommendation-db pg_dump -h localhost -U recommendation recommendation | gzip -9 > $FILENAME
echo "Done"