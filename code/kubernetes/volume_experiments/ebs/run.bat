kubectl apply -f pv-deployment.yaml
kubectl get pvc
kubectl get pv

kubectl get job anthony-test-pvc-file-writer
kubectl describe job anthony-test-pvc-file-writer

kubectl create -f read-deployment.yaml
kubectl describe job anthony-test-pvc-file-reader
