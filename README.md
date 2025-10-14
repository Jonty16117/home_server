

**🚀 Home Server Setup with Cloudflare and Docker 🚀**

**Overview**
------------

This project showcases a comprehensive home server setup using Docker, Cloudflare, and various other technologies. The setup provides a secure, scalable, and maintainable infrastructure for hosting multiple services, including a Rocket.Chat instance, a MongoDB database, and an Nginx reverse proxy.

**Features**
------------

* **Cloudflare Tunneling**: Securely exposes services to the internet using Cloudflare's tunneling feature.
* **Dockerized Services**: Utilizes Docker to containerize services, ensuring isolation, scalability, and easy maintenance.
* **Rocket.Chat**: A self-hosted communication platform for team collaboration.
* **MongoDB**: A NoSQL database for storing and managing data.
* **Nginx Reverse Proxy**: Acts as a reverse proxy, routing traffic to the Rocket.Chat instance.
* **Automatic Certificate Management**: Uses Cloudflare's SSL/TLS certificates for secure communication.

**Technical Details**
--------------------

* **Docker Compose**: Used to define and manage the services and their dependencies.
* **Cloudflare**: Provides tunneling, SSL/TLS certificates, and DNS management.
* **Nginx**: Configured as a reverse proxy to route traffic to the Rocket.Chat instance.
* **Rocket.Chat**: Deployed using the official Docker image.
* **MongoDB**: Deployed using the official Docker image.

**Benefits**
------------

* **Improved Security**: Cloudflare's tunneling feature and SSL/TLS certificates ensure secure communication.
* **Scalability**: Dockerized services allow for easy scaling and resource allocation.
* **Easy Maintenance**: Docker Compose simplifies service management and updates.
* **Flexibility**: Supports multiple services and can be easily extended to accommodate new ones.

**Showcase**
------------

This project demonstrates expertise in:

* Containerization using Docker
* Cloudflare tunneling and SSL/TLS certificate management
* Nginx reverse proxy configuration
* Rocket.Chat and MongoDB deployment
* Docker Compose and service management

**Getting Started**
-------------------

1. Clone the repository.
2. Create a Cloudflare account and obtain a tunnel token.
3. Update the `docker-compose.yml` file with your Cloudflare tunnel token and other environment variables.
4. Run `docker-compose up -d` to start the services.



**License**
----------

This project is licensed under the Apache License. See the LICENSE file for details.

**Usage**
---------

To boostrap a new service, run: `./template/create-service.sh <service-name>`

**Acknowledgments**
------------------

* Cloudflare for their tunneling feature and SSL/TLS certificates.
* Docker for their containerization platform.
* Rocket.Chat and MongoDB for their official Docker images.
* Nginx for their reverse proxy software.