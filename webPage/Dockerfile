FROM python:python:3.11.3
WORKDIR .
RUN apt-get update
COPY static/ .
COPY templates/ .
COPY apiRequest.py .
COPY confLoader.py .
COPY console.py .
COPY front.py .
copy requirements.txt .
RUN pip3 install -r requirements.txt
CMD [ "python","front.py" ]