https://medium.com/@ange.cesari/how-to-deploy-outline-wiki-fully-self-hosted-no-tls-with-docker-compose-e50b57baaf73

## reset admin password
docker exec k8base-db-1 psql -U wiki -d wiki -c "UPDATE users SET password = 'hashed-password' WHERE email = 'admin-email';"

## open db
psql -U wikijs -d wiki -h localhost

## setup of wikijs using keycloak tutorial
https://gist.github.com/Sherex/283d1e4ef07b2bf0a930417dc0117238

## show all login methods uri (in case if its enabled in the settings, otherwise manually update it in database)
https://k8base.xxxxxxx.xxx/login?all
