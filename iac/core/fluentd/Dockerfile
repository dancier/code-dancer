# fluentd/Dockerfile

FROM fluent/fluentd:v1.15.0-1.0
USER root
RUN ["gem", "install", "elasticsearch", "--version", "8.5.1"]
RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-document"]
USER fluent

