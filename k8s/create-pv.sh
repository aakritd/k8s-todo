echo "creating persistent volume and it's claim for database..."

kubectl apply -f ./database/persistentvolume.yml
kubectl apply -f ./database/persistentvolumeclaim.yml

echo "persistent volume and it's claim for database created"