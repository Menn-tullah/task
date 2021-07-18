# Halan's Task

## Part 1: 

* I used Fast API Python library for the Restful API.
* I also used the Pychopg2 library to connect to the Postgresql DB
* In addition, I used Uvicorn for the server implementation.
* It is important to note that I take the Postgres DB’s username and password from the environment variables that are supplied from Kubernetes using secrets.
* I dockerized this app and pushed the image to Docker Hub [link](https://hub.docker.com/r/menntullah/halan-api)


## Part 2:

### 1. Making the cluster:
> * I set up 3 VMs on VirtualBox
> * I set up two networks. The first is the bridge adapter to put the VMs on the same network as the host machine. It enabled the VMs to access the internet and to be able to ssh into the VMs. The second network is to be a host only adapter to connect all the cluster machines together with a static IP.

### 2. Setting up the machines:
> * I made a bash file to facilitate installing the requirements on the VMs (Master and slaves) like ssh,docker,kubeadm,kublet, ..etc. This file is in this path kubeadm_cluster_setup/requirements_installation.sh.        
> * Setup up the master (commands in this file with comments : kubeadm_cluster_setup/master_setup.txt)         
>> * Downloaded calico.yaml for kubernetes networks
>> * Generated the cluster configuration yaml file from kubeadm
>> * Edited the config file with master IP
>> * Initialized kubeadm with kube init command 
>> * Configure our account on the Control Plane Node to have admin access to the API server from a non-privileged account with kubeadm’s recommended commands that were printed from init command
>> * Created a token with kubeadm and printed the join command
> * Setup the nodes (commands in this file with comments : kubeadm_cluster_setup/slave_setup.txt)
>>* After setup, I ran the join command that was printed with kubeadm

### 3. Prepare helm chart for deployment
> * I used bitnami/postgres helm chart to setup my DB as it was convenient and provided the option to make read replicas 
> * I provided the username, password, size, and read replication in the values.yaml to setup both the master and read replicas
> * I made a deployment for my app that utilizes the postgres secret file to insert the passwords into the environment.
> * The deployment has pod antiafinity setup to make sure that pods of the same deplyment run on different nodes.
> * I made a service to this deployment to the outside world
> * I downloaded an nginx ingress controller file and inserted it in the templates [link](https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.48.1/deploy/static/provider/baremetal/deploy.yaml)
> * I wrote the ingress.yaml. 

