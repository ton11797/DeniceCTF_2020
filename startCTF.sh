#!/bin/sh -e

#build
echo "\033[0;32mBuild web1\033[0m"
cd ./web1/
bash build.sh
cd ..
echo "\033[0;32mBuild web2\033[0m"
cd ./web2/
bash build.sh
cd ..
echo "\033[0;32mBuild web3\033[0m"
cd ./web3/
bash build.sh
cd ..
echo "\033[0;32mBuild logic\033[0m"
cd ./logic1/
bash ./build.sh
cd ..

#start
echo "\033[0;32mStart web1\033[0m"
cd ./web1/
docker-compose up -d 
cd ..
echo "\033[0;32mStart web2\033[0m"
docker run -d -p 6903:3003 --name CTF_web2 ctf_web2
echo "\033[0;32mStart web3\033[0m"
docker run -d -p 6980:80 --name CTF_web3 ctf_web3
echo "\033[0;32mStart logic\033[0m"
docker run -d -p 6900:3000 --name CTF_logic ctf_logic