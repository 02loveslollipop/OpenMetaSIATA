sudo apt update
sudo apt install docker-compose
sudo docker build -t OpenMetaSIATA/API:1.0.0beta api/ -p 5000:5000
sudo docker build -t OpenMetaSIATA/DB:1.0.0beta db/ -p 6969:6969
sudo docker build -t OpenMetaSIATA/WEB:1.0.0beta webPage/ -p 80:80
