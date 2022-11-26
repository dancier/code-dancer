cd /run-env
NOW=$(date +"%Y-%m-%d-%H-%M-%S")
FILENAME=db_dump_chat_dancer_${NOW}.sql
echo "Dumping into ${FILENAME}"
docker exec chat-dancer-db pg_dump -h localhost -U chat-dancer chat-dancer > $FILENAME
echo "Done"