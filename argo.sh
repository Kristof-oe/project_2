#!/bin/sh



kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

kubectl get namespace argocd

kubectl get svc -n argocd

kubectl port-forward -n argocd svc/argocd-server 8082:443

sleep 2

kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath={'.data.password'} | base64 --decode &&  echo

