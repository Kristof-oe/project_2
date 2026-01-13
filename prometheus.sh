#!/bin/sh

helm upgrade --install monitoring prometheus-community/kube-prometheus-stack \ 
-f infra/monitoring/values.yaml
sleep 10
kubectl expose service grafana --type=NodePort --target-port=3000 --name=grafana-ext
# kubectl port-forward deployment/prometheus-grafana 3000