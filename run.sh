#!/bin/bash

docker compose down --removes-orphans
docker compose up --build -d

docker exec ${CONTAINER_BE_NAME} web python manage.py migrate