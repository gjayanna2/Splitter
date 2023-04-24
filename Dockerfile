# syntax=docker/dockerfile:1
FROM ubuntu:latest

# set working directory
WORKDIR /katana

# install bot dependencies
COPY requirements.txt .
RUN apt-get update && apt-get install -y python3 
RUN apt-get -y install python3-pip
RUN pip install -r requirements.txt
RUN apt-get -y install ffmpeg

# copy bot files
COPY . .

# final configuration
EXPOSE 8000
CMD python3 bot.py
