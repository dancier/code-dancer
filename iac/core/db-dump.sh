NOW=$(date +"%Y-%m-%d-%H-%M")

docker exec dancer-db pg_dump -h localhost -U dancer dancer > db_dump_${NOW} 