#!/bin/sh
export APP_HOME="$(cd "`dirname "$0"`"/..; pwd)"
export PROJECT=seldon-apps
export DEPLOY_FILE=seldon_deployment_iris_model.json

# deploy to k8s
kubectl create -f "${APP_HOME}"/test/${DEPLOY_FILE} --namespace ${PROJECT}

# test with seldon core serving
# http://<ambassadorEndpoint>/seldon/<namespace>/<deploymentName>/api/v0.1/predictions
curl http://$(minikube ip):$(kubectl get svc ambassador -n ambassador -o jsonpath='{.spec.ports[0].nodePort}')/seldon/seldon-apps/serving-iris-demo/api/v0.1/predictions \
    --request POST \
    --header "Content-Type: application/json" \
    --data '{"data":{"ndarray":[[1.0,2.0, 3.0, 4.0]]}}' 
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

# delete deploy
# kubectl delete -f "${APP_HOME}"/test/${DEPLOY_FILE} --namespace ${PROJECT}