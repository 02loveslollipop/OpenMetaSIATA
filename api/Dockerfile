FROM python:python:3.11.3
RUN apt-get update
WORKDIR .
COPY api.py .
COPY config.yml .
COPY confLoader.py .
COPY console.py .
COPY example_config.yml .
COPY UpdateThread.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
CMD [ "python","api.py" ]
