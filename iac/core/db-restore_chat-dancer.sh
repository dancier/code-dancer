docker exec -i chat-dancer-db psql -h localhost -U chat-dancer postgres << SQL
-- https://stackoverflow.com/questions/17449420/postgresql-unable-to-drop-database-because-of-some-auto-connections-to-db

REVOKE CONNECT ON DATABASE chat-dancer FROM public;

SELECT pid, pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = 'chat-dancer' AND pid <> pg_backend_pid();

drop database chat-dancer;

create database chat-dancer;

GRANT CONNECT ON DATABASE chat-dancer TO public;

SQL


echo "Restoring from ${1}"

cat $1 | gunzip - | docker exec -i chat-dancer-db psql chat-dancer -h localhost -U chat-dancer -b -f -
echo "Done"
