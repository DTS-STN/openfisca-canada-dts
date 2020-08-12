## Setup OpenFisca canada to run in docker

## Run the application locally using Docker

- [Install Docker](https://www.docker.com/get-started)
- Build the docker image: `docker build . -t openfisca-canada`
- Run the image: `docker run -it -p 5000:5000 openfisca-canada`
- Access the API url from: http://localhost:5000 or http://localhost:5000/spec

## Run the application using Docker Compose

This implementation uses a mounted volume for your country rules and tests which means that tests can be written and run without the need to rebuild the container.

 - [Install Docker-Compose](https://docs.docker.com/compose/install/)
 - To build/rebuild container run make command: `make build-run-dev`
 - To run tests run make command: `make test`
 - Access the API url from: http://localhost:5000 or http://localhost:5000/spec


