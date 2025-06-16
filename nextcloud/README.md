## Clone latest version to ./data using:
- git clone --branch v31.0.6 --single-branch --depth 1 https://github.com/nextcloud/server.git nextcloud

## Then manually update the config in ./data/nextcloud/config/config.php from ./config/ files

## Before starting the nextcloud container, run this in ./data
- sudo rm -rf ./nextcloud*

## Setup db
- sudo rm -rf ./mysql && sudo mkdir -p ./mysql && sudo chown -R 65532:65532 ./mysql && sudo chmod -R 755 ./mysql