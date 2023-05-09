sudo apt update
sudo apt install docker-compose -y
sudo apt install python3 -ya
sudo python3 setup.py
#Building of images
sudo docker build -t openmetasiata/api:1.0.0beta api/ 
sudo docker build -t openmetasiata/db:1.0.0beta db/ 
sudo docker build -t openmetasiata/web:1.0.0beta webPage/
#Runing docker-compose
sudo docker-compose -f docker-compose.yml up -d