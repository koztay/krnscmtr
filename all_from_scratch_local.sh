#!/usr/bin/env bash
eval $(docker-machine env karnas)
# eval $(docker-machine env istebu)
# Stop and remove all containers
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

# Delete all images
docker rmi -f $(docker images -q)

# Delete all volumes
docker volume ls -qf dangling=true | xargs docker volume rm

# Build with no-cache
docker-compose -f dev.yml build
# Build without no-cache
#docker-compose -f docker-compose-production.yml build
# Up containers
docker-compose -f dev.yml up -d
