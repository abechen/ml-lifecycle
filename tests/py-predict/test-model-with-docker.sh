#!/bin/sh
export APP_HOME="$(cd "`dirname "$0"`"/..; pwd)"
export IMAGE_NAME=abechen/serving-iris-demo
export IMAGE_VERSION=latest

# run wrapper docker image
docker run --name "iris_predictor" --rm -p 5001:5000 ${IMAGE_NAME}:${IMAGE_VERSION}

# test wuth docker
curl http://0.0.0.0:5001/predict \
    --data 'json={"data":{"ndarray":[[1.0, 2.0, 3.0, 4.0]]}}'
: '{
    "data": {
        "names": ["iris-setosa","iris-vericolor","iris-virginica"],
        "ndarray": [
            [0.0011089286758401262,0.012902008299819315,0.9859890630243405]
        ]
    },
    "meta": {}
}'
