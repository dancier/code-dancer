cd /run-env/db-dump
NOW=$(date +"%Y-%m-%d-%H-%M-%S")
FILENAME=db_dump_chat_dancer_${NOW}.sql.gz
echo "Dumping into ${FILENAME}"
docker exec chat-dancer-db pg_dump -h localhost -U chat-dancer chat-dancer | gzip -9 > $FILENAME
echo "Done"