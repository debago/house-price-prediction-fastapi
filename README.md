# run fastapi:

1. uvicorn app_fastapi:app --reload
2. uvicorn app_fastapi:app --host 0.0.0.0 -port 8000 --reload


# Login to azure vm

ssh -i <private-pem key> azureuser@vm-public-ip

# inside vm

sudo apt udate
sudo apt install -y docker.io
docker version
sudo systemctl enable docker
sudo systemctl start docker

# Avoid typing sudo everytime

sudo usermod -aG docker $USER
exit

Reconnect via SSH

sudo apt install -y docker-compose
docker-compose --version

docker-compose up --build -d (detached mode)
docker-compose up --build 

docker-compose config