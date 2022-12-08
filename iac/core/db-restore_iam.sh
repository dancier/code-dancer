docker exec -i dancer-db psql -h localhost -U dancer postgres << SQL
-- https://stackoverflow.com/questions/17449420/postgresql-unable-to-drop-database-because-of-some-auto-connections-to-db

REVOKE CONNECT ON DATABASE keycloak FROM public;

SELECT pid, pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = 'keycloak' AND pid <> pg_backend_pid();

drop database keycloak;

create database keycloak;

GRANT CONNECT ON DATABASE keycloak TO public;

SQL


echo "Restoring from ${1}"

cat $1 | gunzip - | docker exec -i iam-db psql keycloak -h localhost -U keycloak -b -f -
echo "Done"
