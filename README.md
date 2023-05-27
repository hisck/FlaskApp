This repository builds a container and pushes it to Docker hub.
It contains a simple hello world application created with Python Flask.

First of all, make sure that you have docker installed, in order to build and run the container locally.

To build the image locally using docker you need to use the following command `sudo docker image build -t flaskappdocker .`

To run the container use the following command `sudo docker run --network host -d flaskappdocker`

The CI provided runs on each push to the main branch and periodically on Saturday at 7 PM (17 PM on UTC timezone).

The link to the docker hub repo is the following https://hub.docker.com/repository/docker/hisckk/flask-app/general
