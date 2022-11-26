cd /run-env
NOW=$(date +"%Y-%m-%d-%H-%M-%S")
FILENAME=db_dump_iam_${NOW}.sql
echo "Dumping into ${FILENAME}"
docker exec iam-db pg_dump -h localhost -U iam iam > $FILENAME
echo "Done"