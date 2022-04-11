
# Finalizar e iniciar um cluster K8s via Minikube
minikube delete 
minikube start

# Ferramentas de monitoramento
kubectl apply -k ./tools/monitoring/

# Aplicação exemplo de Monitoramento de Falhas
kubectl apply -f ./k8s/

# Configurando porta para acesso externo ao cluster
kubectl port-forward failuremanager-6f5cf54dc-tdbp6 31199:31199

# Acessando a porta anterior pelo navegador ou outra CLI
http://localhost:31199/docs