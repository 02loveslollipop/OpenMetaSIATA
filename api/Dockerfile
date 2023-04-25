FROM ubuntu
RUN apt update
RUN apt install python3.10 -y
RUN apt install python3-pip -y
WORKDIR /api
COPY api.py .
COPY requirements_api.txt .
RUN pip3 install -r requirements_api.txt
CMD [ "python3.10","api.py" ]
