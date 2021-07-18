sudo apt-get -y update
sudo apt-get -y install curl
sudo apt -y install net-tools
sudo apt -y install ssh
sudo apt-get -y install vim

# disable swap
sudo swapoff -a
sudo vim /etc/fstab

# install docker
sudo apt-get update
sudo apt -y install docker.io
sudo systemctl start docker
sudo systemctl enable docker

#install kubeadm,kubelet,kubectl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add
sudo apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"
sudo apt-get install -y kubeadm kubelet kubectl
sudo apt-mark hold kubelet kubeadm kubectl docker
