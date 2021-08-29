FROM python:3.7.11-alpine3.14

WORKDIR /app

### EDIT THIS ###
ENV PROC=1
ENV THREAD=1
ENV SLEEP=0.001
ENV COUNT=2
#################

COPY requirements.txt /tmp/
RUN pip3 install --requirement /tmp/requirements.txt
COPY dos.py .
COPY payload.py .
COPY /config ./config
COPY /helpers ./helpers

CMD ["sh", "-c", "./dos.py -p $PROC -t $THREAD -s $SLEEP -c $COUNT"]
