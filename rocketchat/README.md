# Before running the mongodb container, create and make the daten folder with the following permissions
sudo mkdir daten && sudo chown -R 1001 ./daten

# Regarding the env var ROOT_URL
After changing it, the db must be reset and both the db and rocketchat containers must be recreated