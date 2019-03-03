#
# Use an Node8 slim
# Stretch is Debian 9
FROM debian:stretch-slim
#FROM node:8.12.0-stretch

LABEL maintainer "Matt Cliff <matt@denvercliffs.com>"

ENV AWSCLI_VERSION "1.16.33"

ENV STACK_NAME awsmyconsole
ENV CI_BUCKET tempawsbuild

RUN \
    apt-get update && \
    apt-get install -y apt-utils less gnupg zip curl python-pip


# custom pip install
#RUN curl -sL https://bootstrap.pypa.io/get-pip.py | /usr/bin/python && \
RUN \
    pip install wheel && \
    pip install setuptools && \
    pip install aws-sam-cli && \
    pip install awscli==$AWSCLI_VERSION

#RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
#    apt-get install -y nodejs
#RUN npm install -g serverless

RUN groupadd -r nonroot -g 59417 && \
    useradd -r -g nonroot -m  -d /nonroot -u 59417 nonroot && \
    chmod -R 777 /nonroot

USER nonroot
ENV PATH $PATH:$HOME/.local/bin
WORKDIR /nonroot

COPY bootstrap.sh /bootstrap.sh
COPY template.yaml /nonroot/template.yaml

#ENTRYPINT [ "localhost" ]
CMD [ "/bootstrap.sh" ]
#CMD [ "sh", "-c", "/bootstrap.sh ${STACK_NAME} ${CI_BUCKET}" ]
:
