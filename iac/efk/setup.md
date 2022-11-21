# Setup

## with already existing volume
new server

* Nürnberg
* Ubuntu
* CX21
* Volumen test-dancelake
* Cloud-init snipped from correct environment
* Servername: test-dancelake

check init-process on host with less +F /var/log/syslog

host will reboot after first initialization has run.

This takes some minutes.

## from scratch

this covers only the docker-compose parts

after first run:
 chown 1000:1000 -R ./volumes/esdata/
(otherwise elastic will not start)


create passwords in container with elasticserach_setup_passwords...

now configure the password where other components connect to elastic