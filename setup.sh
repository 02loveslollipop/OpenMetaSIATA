sudo apt update
sudo apt install docker-compose
sudo docker build -t openmetasiata/api:1.0.0beta api/ 
sudo docker build -t openmetasiata/db:1.0.0beta db/ 
sudo docker build -t openmetasiata/web:1.0.0beta webPage/

sudo docker run -d -p 5000:5000  openmetasiata/api:1.0.0beta
sudo docker run -d -p 6969:6969 openmetasiata/db:1.0.0beta
sudo docker run -d -p 80:80 openmetasiata/web:1.0.0beta