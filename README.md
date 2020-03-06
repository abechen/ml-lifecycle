# Machine Learning Lifecycle Demo

using seldon core and mlflow

Required to install:

* pip
* miniconda
* s2i
* docker engine
* kubectl
* helm
* k8s
* seldon-core

## pip

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

## k8s

---

Before anything, we will first set up the k8s cluster.
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
