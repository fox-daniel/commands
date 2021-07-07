# Kubernetes (K8s)
## Opensource Automated container deployment, scaling, management, for groups of containers

## [Tutorial](https://kubernetes.io/docs/tutorials/kubernetes-basics/)

### Kubernetes cluster components:
- Control Plane
- Nodes: VMs or Physical Machine that is a Worker
	- Kubelet: manage node and communicate with Control Plane through Kubernetes API
	- Tools for container apps, e.g. Docker
	- Production Traffice: >2 nodes

Once a cluster is running:

### Deployment
- create deployment configuration
- deployment controller monitors and replaces nodes if they go down
- Docker containers
	- Docker is a container runtime that unpacks the container and runs the app
- NGINX for load balancing
- Pod (logical host): >0 application containers and resources on a single node
	- Storage
	- Networking (containers in a pod share IP Address) 
	- Container Run Instructions 

### Expose an App through a _Service_
- pass

### Scale - change number of replicas in a deployment
- Increase number of pods
- autoscaling exists
- allows rolling updates without downtime

### Rolling Updates: updates without downtime
- requires multiple instances
- versioned





