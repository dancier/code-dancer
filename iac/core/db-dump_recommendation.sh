cd /run-env
NOW=$(date +"%Y-%m-%d-%H-%M-%S")
FILENAME=db_dump_recommendation_${NOW}.sql.gz
echo "Dumping into ${FILENAME}"
docker exec recommendation-db pg_dump -h localhost -U recommendation recommendation | gzip -9 > $FILENAME
echo "Done"