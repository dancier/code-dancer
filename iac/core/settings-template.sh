###################################
# Dancer DB
###################################

export DANCER_DB_HOSTNAME=dancer-db
export DANCER_DB_USER=dancer
export DANCER_DB_PASSWORD=secret
export DANCER_DB_DB=dancer

###################################
# Dancer Service
###################################

export DANCER_APP_COOKIE_SECURE=false
export DANCER_APP_COOKIE_SAMESITE=None
export SPRING_DATASOURCE_URL=jdbc:postgresql://${DANCER_DB_HOSTNAME}:5432/${DANCER_DB_DB}
export SPRING_DATASOURCE_USERNAME=${DANCER_DB_USER}
export SPRING_DATASOURCE_PASSWORD=${DANCER_DB_PASSWORD}
export APP_AUTH_TOKENSECRET=adfjasödfjasöljföasjflasjdflkjaslkfjaslfjladsjf
export APP_CORS_ALLOWED_ORIGINS=https://test.dancier.net
export SPRING_PROFILES_ACTIVE=staging,json-logging
export APP_MAIL_USER=dev@dancier.net
export APP_MAIL_PASS=whatever
export APP_CAPTCHA_APIKEY=captcha-api-key
export DANCER_TAG=latest
export APP_CAPTCHA_MAGICTOKEN=secret
export APP_ADMIN_EMAIL=marc@becheftigt.de
export APP_ADMIN_PASS=secret
export BACKEND_HOSTNAME=dancer.dancier.net
export DANCIER_TOKEN_URI=https://test-iam.dancier.net/realms/dancier/protocol/openid-connect/token

################################
# Chat Dancer DB
################################
export CHAT_DANCER_DB_HOSTNAME=chat-dancer-db
export CHAT_DANCER_DB_USER=chat-dancer
export CHAT_DANCER_DB_PASSWORD=secret
export CHAT_DANCER_DB_DB=chat-dancer

###############################
# Chat-Dancer Service
###############################

export CHAT_DANCER_TAG=1.0
export CHAT_DANCER_SPRING_DATASOURCE_URL=jdbc:postgresql://${CHAT_DANCER_DB_HOSTNAME}:5432/${CHAT_DANCER_DB_DB}
export CHAT_DANCER_SPRING_DATASOURCE_USERNAME=${CHAT_DANCER_DB_USER}
export CHAT_DANCER_SPRING_DATASOURCE_PASSWORD=${CHAT_DANCER_DB_PASSWORD}

###################################
# PG Admin
###################################

export PG_ADMIN_PASSWORD=secret
export PG_ADMIN_OAUTH2_SECRET=secret
export PG_ADMIN_OAUTH2_TOKEN_URL=https://test-iam.dancier.net/realms/dancier/protocol/openid-connect/token
export PG_ADMIN_OAUTH2_AUTHORIZATION_URL=https://test-iam.dancier.net/realms/dancier/protocol/openid-connect/auth
export PG_ADMIN_OAUTH2_API_BASE_URL=https://test-iam.dancier.net/realms/dancier
export PG_ADMIN_OAUTH2_USERINFO_ENDPOINT=https://test-iam.dancier.net/realms/dancier/protocol/openid-connect/userinfo
export PG_ADMIN_OAUTH2_SERVER_METADATA_URL=https://test-iam.dancier.net/realms/dancier/.well-known/openid-configuration
export PG_ADMIN_HOSTNAME=pgadmin.dancier.net


##################################
# Fluentd
##################################

export ELASTIC_HOST=elastic.dancier.net
export ELASTIC_USER=elastic
export ELASTIC_PASS=secret


##################################
# Show Dancer
##################################

export SHOW_DANCER_HOSTNAME=dancier.net
export SHOW_DANCER_TAG=latest
export DANCIER_BACKEND_URL=https://dancer.dancier.net

##################################
# IAM
##################################

export IAM_ADMIN_PASSWD=foobar123
export IAM_HOST=iam.dancier.net

####################################
# S3
####################################

export S3_ADMIN_PASSWD=secret
export S3_HOST=test-s3.dancier.net
export S3_UI_HOST=test-s3-ui.dancier.net
export S3_CLIENT_SECRET=secret
export S3_OPENID_CONFIG_URL=https://test-iam.dancier.net/realms/dancier/.well-known/openid-configuration

####################################
# Recommendation DB
####################################

export RECOMMENDATION_DB_USER=recommendation
export RECOMMENDATION_DB_PASSWORD=secret
export RECOMMENDATION_DB=recommendation

####################################
# Recommendation
####################################

export RECOMMENDATION_S3_SECRET=geheim
export RECOMMENDATION_S3_TOKENURI=https://test-iam.dancier.net/realms/dancier/protocol/openid-connect/token
export RECOMMENDATION_S3_STS_ENDPOINT=https://test-s3.dancier.net
export RECOMMENDATION_S3_HOST=test-s3.dancier.net
export RECOMMENDATION_TAG=latest

#####################################
# Kafka UI
#####################################

export KAFKA_UI_HOSTNAME=test-kafka-ui.dancier.net

#####################################
# S3
#####################################

export S3_OIDC_CLIENT_ID=s3

#################################
# Kikeriki
#################################

export KIKERIKI_TAG=latest
export KIKERIKI_DB_HOSTNAME=kikeriki-db

#################################
# Kikeriki DB
#################################

export KIKERIKI_DB_USER=kikeriki
export KIKERIKI_DB_PASSWORD=secrect
export KIKERIKI_DB_DB=kikeriki

##################################
# Prometheus
##################################

export PROMETHEUS_UI_HOST=test-prometheus.dancier.net

export RUN_ENV=/run-env



