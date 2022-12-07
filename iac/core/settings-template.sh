export DANCER_DB_HOSTNAME=dancer-db
export DANCER_DB_USER=dancer
export DANCER_DB_PASSWORD=secret
export DANCER_DB_DB=dancer

export PG_ADMIN_PASSWORD=secret

export SPRING_DATASOURCE_URL=jdbc:postgresql://${DANCER_DB_HOSTNAME}:5432/${DANCER_DB_DB}
export SPRING_DATASOURCE_USERNAME=${DANCER_DB_USER}
export SPRING_DATASOURCE_PASSWORD=${DANCER_DB_PASSWORD}

export APP_AUTH_TOKENSECRET=adfjasödfjasöljföasjflasjdflkjaslkfjaslfjladsjf

export APP_CORS_ALLOWED_ORIGINS=https://test.dancier.net

export SPRING_PROFILES_ACTIVE=staging,json-logging

export APP_MAIL_USER=dev@dancier.net
export APP_MAIL_PASS=whatever

export APP_CAPTCHA_APIKEY=captcha-api-key

# for delivering the files
export ELASTIC_HOST=elastic.dancier.net
export ELASTIC_USER=elastic
export ELASTIC_PASS=secret

export BACKEND_HOSTNAME=dancer.dancier.net

export PG_ADMIN_HOSTNAME=pgadmin.dancier.net

export SHOW_DANCER_HOSTNAME=dancier.net

export DANCER_TAG=1.0

export TRAEFIK_TAG=traefik

export SHOW_DANCER_TAG=show-dancer

export SHOW_DANCER_DEPLOY_TAG=1.0

export DANCIER_BACKEND_URL=https://dancer.dancier.net

export IAM_ADMIN_PASSWD=foobar123

export IAM_HOST=iam.dancier.net

export S3_ADMIN_PASSWD=secret

export S3_HOST=test-s3.dancier.net

export S3_UI_HOST=test-s3-ui.dancier.net

export S3_CLIENT_SECRET=secret

export S3_OPENID_CONFIG_URL=https://test-iam.dancier.net/realms/dancier/.well-known/openid-configuration

export PG_ADMIN_OAUTH2_SECRET=secret

export PG_ADMIN_OAUTH2_TOKEN_URL=https://test-iam.dancier.net/realms/dancier/protocol/openid-connect/token

export PG_ADMIN_OAUTH2_AUTHORIZATION_URL=https://test-iam.dancier.net/realms/dancier/protocol/openid-connect/auth

export PG_ADMIN_OAUTH2_API_BASE_URL=https://test-iam.dancier.net/realms/dancier

export PG_ADMIN_OAUTH2_USERINFO_ENDPOINT=https://test-iam.dancier.net/realms/dancier/protocol/openid-connect/userinfo

export APP_CAPTCHA_MAGICTOKEN=secret

export APP_ADMIN_EMAIL=marc@becheftigt.de

export APP_ADMIN_PASS=secret

export RECOMMENDATION_DB_USER=recommendation

export RECOMMENDATION_DB_PASSWORD=secret

export RECOMMENDATION_DB=recommendation

export CHAT_DANCER_DB_USER=chat-dancer

export CHAT_DANCER_DB_PASSWORD=secret

export CHAT_DANCER_DB=chat-dancer

export DANCIER_TOKEN_URI=https://test-iam.dancier.net/realms/dancier/protocol/openid-connect/token

export S3_OIDC_CLIENT_ID=s3

export RECOMMENDATION_S3_SECRET=geheim

export RECOMMENDATION_S3_TOKENURI=https://test-iam.dancier.net/realms/dancier/protocol/openid-connect/token

export RECOMMENDATION_S3_STS_ENDPOINT=https://test-s3.dancier.net

export RECOMMENDATION_S3_HOST=test-s3.dancier.net

export KAFKA_UI_HOSTNAME=test-kafka-ui.dancier.net

export COMPOSE_HTTP_TIMEOUT=120

export RECOMMENDATION_TAG=latest

export DANCER_DB_TAG=dancer-db

export CHAT_DANCER_TAG=1.0

export CHAT_DANCER_DB=chat-dancer-db

export RECOMMENDATION_DB_TAG=recommendation-db

export IAM_TAG=iam

export IAM_DB_TAG=iam-db

export S3_TAG=s3

export KAFKA_TAG=kafka

export KAFKA_UI_TAG=kafka-ui

export PROMETHEUS_TAG=prometheus

export RUN_ENV=/run-env

export KIKERIKI_TAG=1.0