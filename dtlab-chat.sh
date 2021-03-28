#!/bin/bash

cd /home
docker build -t python392slim .
docker run -d -p 5000:5000 --name DTLab-chat python392slim
docker ps -a