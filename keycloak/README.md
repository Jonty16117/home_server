https://medium.com/@ange.cesari/how-to-deploy-outline-wiki-fully-self-hosted-no-tls-with-docker-compose-e50b57baaf73

https://wenkdth.org/posts/keycloak-outline-setup/#oidc-config

# reset admin user/passord
- go to postgres container
- run "psql -U <username> <mydatabase>" (in our case: "psql -U keycloak -d keycloak")
- then run "TRUNCATE USER_ENTITY CASCADE;"
- then restart the keycloak container, it will create the admin user from .env creds