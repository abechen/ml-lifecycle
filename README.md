# Machine Learning Lifecycle Demo

TODO: desc

---

Required to install:

* s2i
* docker engine
* kubectl
* helm
* kubernetes
* seldon-core

---

## s2i

```=shell
brew install source-to-image
```

---

## docker engine

Go to Docker official web site & base on your OS to download and install “Docker Community Edition”
- https://store.docker.com/search?type=edition&offering=community

---

## kubectl

```=shell
brew install kubectl

# Test to ensure the version you installed is up-to-date:
kubectl version --client
```

---

## helm

---

```=shell
# install tiller
kubectl create serviceaccount --namespace kube-system tiller
kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller

# install heml v2
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get | bash
helm init --history-max 200 && sleep 30

kubectl patch deploy --namespace kube-system tiller-deploy -p '{"spec":{"template":{"spec":{"serviceAccount":"tiller"}}}}'
```

## kubernetes

---

Before anything, we will first set up the kubernetes cluster.
Firstly, we will create a cluster using minikube.

```=shell
# Install minikube
brew install minikube

# Create k8s cluster
minikube start \
  --vm-driver=virtualbox \
  --cpus=4 \
  --memory=8192

# (optional) Start k8s dashboard
minikube dashboard
```

---

## seldon core

Seldon Core is a open-source platform for rapidly deploying machine learning models on Kubernetes.

- [official website](https://www.seldon.io/tech/products/core/)
- [github](https://github.com/SeldonIO/seldon-core)

---

### Install seldon core

```=shell
export VERSION=0.4.1

helm install seldon-core-operator --name seldon-core --version ${VERSION} --repo https://storage.googleapis.com/seldon-charts --set usageMetrics.enabled=true --namespace seldon-system
```

### (Optional) Install redis for model persistence

```=shell
helm install --name redis stable/redis --namespace redis
helm install stable/redis-ha --name=redis-ha --namespace=redis
```

### (Optional) Seldon core analytics

```=shell
export VERSION=0.4.1

# Install seldon core analytics
helm install seldon-core-analytics --name seldon-core-analytics  --version ${VERSION} --set grafana_prom_admin_password=admin --set persistence.enabled=false --repo https://storage.googleapis.com/seldon-charts --namespace seldon-core-analytics

# To access the Grafana dashboard port-forward to the Grafana pod:
kubectl port-forward $(kubectl get pods -l app=grafana-prom-server -n seldon-core-analytics -o jsonpath='{.items[0].metadata.name}') -n seldon-core-analytics 3000:3000

# Open grafana web (user/password: admin/admin)
http://localhost:3000/d/0tL8wPXWz/prediction-analytics?refresh=5s&orgId=1
```
