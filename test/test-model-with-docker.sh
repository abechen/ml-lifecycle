#!/bin/sh
export APP_HOME="$(cd "`dirname "$0"`"/..; pwd)"
export IMAGE_NAME=cathay/sklearn-iris
export IMAGE_VERSION=0.1

# run wrapper docker image
docker run --name "iris_predictor" --rm -p 5001:5000 ${IMAGE_NAME}:${IMAGE_VERSION}

# test wuth docker
curl http://0.0.0.0:5001/predict \
    --data 'json={"data":{"ndarray":[[1.0,2.0, 3.0, 4.0]]}}' 
: '{
    "data":{
        "names":[
        "iris-setosa",
        "iris-vericolor",
        "iris-virginica"
        ],
    "ndarray":[
        [
            0.0364996395323677,
            0.00964742714103532,
            0.953852933326597
        ]
    ]
    },
    "meta":{
    }
}'