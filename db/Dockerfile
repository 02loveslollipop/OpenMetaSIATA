FROM python:3.11.3
WORKDIR .
RUN apt-get update
COPY db.py .
COPY database.py .
COPY config.yml .
COPY confLoader.py .
COPY console.py .
COPY example_config.yml .
COPY requirements.txt .
COPY users.csv .
RUN pip3 install -r requirements.txt
CMD [ "python","db.py" ]