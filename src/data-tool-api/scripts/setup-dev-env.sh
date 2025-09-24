#!/bin/bash
# #########################
# Set up dev environment
# #########################

docker-compose -f ./scripts/docker-compose-dev.yml down && docker-compose -f ./scripts/docker-compose-dev.yml up -d

