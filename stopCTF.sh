#!/bin/sh -e

#build
echo "\033[0;32mStop web1\033[0m"
cd ./web1/
docker-compose stop 
cd ..
echo "\033[0;32mStop web2\033[0m"
docker stop CTF_web2
echo "\033[0;32mStop web3\033[0m"
docker stop CTF_web3
echo "\033[0;32mStop logic\033[0m"
docker stop CTF_logic
docker rm CTF_web2
docker rm CTF_web3
docker rm CTF_logic