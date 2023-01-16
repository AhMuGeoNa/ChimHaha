#!/bin/sh

echo "실행 코드가 있는 곳으로 이동 \n"
cd /config/workspace/project/ChimHaha

echo 현재 작업 디렉토리 입니다.
pwd

if [ -d /config/workspace/project/ChimHaha/log ]; then
    echo "\n로그를 저장할 폴더가 이미 존재합니다 \n"
else
    mkdir /config/workspace/project/ChimHaha/log
    echo "\n로그를 저장할 폴더가 존재하지 않아 생성하였습니다. \n"
fi

today=$(date "+%Y-%m-%d")
echo ${today}

chain_path="../utils/keys/cert/fullchain1.pem"
key_path="../utils/keys/cert/privkey1.pem"

echo "\n침하하 ssl 서버를 실행합니다."
nohup python manage.py runsslserver --certificate $chain_path \
    --key $key_path 0:9330 > /config/workspace/project/ChimHaha/log/${today}_django.out &