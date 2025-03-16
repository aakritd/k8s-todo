#####################

echo "creating resources for database..."

echo "creating deployment for database..."

kubectl apply -f ./database/deployment.yml

echo "deployment for database created"

echo "creating service for database..."

kubectl apply -f ./database/service.yml

echo "service for database created"

echo "resources for database created"

#####################

echo "creating resources for backend..."

echo "creating deployment for backend..."

kubectl apply -f ./backend/deployment.yml

echo "deployment for backend created"

echo "creating service for backend..."

kubectl apply -f ./backend/service.yml

echo "service for backend created"

echo "resources for backend created"

#####################

echo "creating resources for frontend..."

echo "creating deployment for frontend..."

kubectl apply -f ./frontend/deployment.yml

echo "deployment for frontend created"

echo "creating service for frontend..."

kubectl apply -f ./frontend/service.yml

echo "service for frontend created"

echo "resources for frontend created"


