#!/bin/sh
export APP_HOME="$(cd "`dirname "$0"`"/..; pwd)"
export REGISTRY_PROJECT=abechen
export IMAGE_NAME=serving-iris-demo

export WRAPPER_BASE_IMAGE=seldonio/seldon-core-s2i-python36:0.13

# move files to target folder for wrap
#TODO

# use s2i to wrap files and base image
s2i build "${APP_HOME}"/target/py-predict ${WRAPPER_BASE_IMAGE} ${IMAGE_NAME}

# deploy docker image to harbor registry
docker tag ${IMAGE_NAME} ${REGISTRY_PROJECT}/${IMAGE_NAME}
docker push ${REGISTRY_PROJECT}/${IMAGE_NAME}
