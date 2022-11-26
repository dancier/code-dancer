cd /run-env
NOW=$(date +"%Y-%m-%d-%H-%M-%S")
FILENAME=db_dump_dancer_${NOW}.sql.gz
echo "Dumping into ${FILENAME}"
docker exec dancer-db pg_dump -h localhost -U dancer dancer | gzip -9 > $FILENAME
echo "Done"