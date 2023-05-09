# OpenMetaSIATA

> A Python based solution to review and watch graphically the river levels using the SIATA API 
> 

## Intro
SIATA have an API that allows to recieve information about all of their services, this solution allows to use this information to have an easier undestanding of this data.

## Requirements

1. A linux based system
2. A MapBox token (Optional if using Guided setup)

# Quick Setup

The repo contain a setup.sh, that allows and help the process of deploy of the services, if you want, it's also possible to manually deploy every container.

1. Clone the repository:

```bash
git clone https://github.com/02loveslollipop/OpenMetaSIATA.git
```

2. Execute the setup script: 

```bash
sudo bash setup.sh
```

3. Select the second option (2.Fast setup (default values))

4. Get your token at [MapBox](https://account.mapbox.com/access-tokens/), it can either be a default token or a custom token

5. Enter your token onto the script

6. Try the front at [localhost:80](http://127.0.0.1:80)

# Guided Setup

The script also allow to do a custom guided setup, this will allow you to control certain configurations of the services, the script will modify the configuration files, build the new dockers and execute the docker-compose.

# Advance Setup
The script allows to create an Advance Setup, this mode will build and execute the docker-compose with the current config.yml of every service, in this mode you must change manually the configurations of ``api/config.yml``, ``db/config.yml`` and ``webPage/config.yml``
``WARNING``: As the script is not modifying the config files, it will not warn of bad configurations.

# Update containers
It can be executed either with the 4th option of ``setup.sh`` or manually executing ``update.sh``
```bash
sudo bash update.sh
```

# Manual setup
If you don't want to use the script to setup the services, you can follow this steps:

1. Install docker-compose onto your system:

    Ubuntu/Debian based distros:
```bash
sudo apt install docker-compose
```
  
    Red Hat Enterprise Linux
```bash
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/rhel/docker-ce.repo
sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo systemctl start docker
```

4. Clone the repository:

```bash
git clone https://github.com/02loveslollipop/OpenMetaSIATA.git
```

3. Manually set-up the configuration files at ``api/config.yml``, ``db/config.yml`` and ``webPage/config.yml``

4. Build the docker images:

```bash
sudo docker build -t openmetasiata/api:1.0.0beta api/ 
sudo docker build -t openmetasiata/db:1.0.0beta db/ 
sudo docker build -t openmetasiata/web:1.0.0beta webPage/
```

5. Modify ``docker-compose.yml``, changing the ports if you made any change in this aspect:

```yaml
siata-web:
  ...
  expose:
    - "<new_web_port>"
  ports:
    - "<new_web_port>:<new_web_port>"
siata-db:
  ...
  expose:
    - "<new_db_port>"
siata-api:
  ...
  expose:
    - "<new_api_port>"
```

6. Start the docker-compose file using:

```bash
sudo docker-compose -f docker-compose.yml up -d
```
