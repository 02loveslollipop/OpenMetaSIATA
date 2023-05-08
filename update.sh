#Stop the docker-compose
sudo docker-compose stop
#Re-build the images
sudo docker build -t openmetasiata/api:1.0.0beta api/ 
sudo docker build -t openmetasiata/db:1.0.0beta db/ 
sudo docker build -t openmetasiata/web:1.0.0beta webPage/
#Execute again the docker-compose
sudo docker-compose -f docker-compose.yml up -d