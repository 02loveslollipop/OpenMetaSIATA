FROM python:python:3.11.3
WORKDIR /db
RUN apt-get update
COPY db.py .
COPY config.yml .
COPY confLoader.py .
COPY console.py .
COPY example_config.yml .
COPY users.csv .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
CMD [ "python","db.py" ]