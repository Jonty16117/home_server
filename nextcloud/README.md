## Clone latest version to ./data using:
- git clone --branch v31.0.6 --single-branch --depth 1 https://github.com/nextcloud/server.git nextcloud

## Then manually update the config in ./data/nextcloud/config/config.php from ./config/ files

## Before starting the nextcloud container, run this in ./data
- sudo rm -rf ./nextcloud*

## Set permissions for nextcloud-config folder
- sudo chown -R www-data:www-data nextcloud-config

## Setup db
- sudo rm -rf ./mysql && sudo mkdir -p ./mysql && sudo chown -R 65532:65532 ./mysql && sudo chmod -R 755 ./mysql

## Reset rate limit for IP
- ./occ security:bruteforce:reset 91.57.70.169 

## reset admin password
- ./occ user:resetpassword admin
