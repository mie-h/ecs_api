#!/bin/bash
echo "building image... "

docker_image_tag = ""
docker build -f Dockerfile -t ${docker_image_tag}
