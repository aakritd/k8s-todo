echo "deleting previously created volumes and namespace..."

kubectl delete pv database-pv -n web-ns
kubectl delete pvc database-pvc -n web-ns

kubectl delete ns web-ns

echo " previously created volumes and namespace deleted"
