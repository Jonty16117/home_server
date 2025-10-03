Role Name
=========

A brief description of the role goes here.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).

#### Backup wireguard
ansible-playbook playbook.yml --tags backup

#### Restore wireguard
ansible-playbook playbook.yml --tags restore


nmcli connection import type wireguard file /etc/wireguard/wg0.conf
nmcli connection modify wg0 ipv4.dns "10.0.0.1" ipv4.ignore-auto-dns yes
nmcli connection modify wg0 ipv6.ignore-auto-dns yes
nmcli connection up wg0
nmcli device show wg0 | grep IP4.DNS


demo vm login:
setup wireguard using client config: http://clouds.beer:10086/#/share?ShareID=c4c53eb1-71f2-469f-a27a-e15b5bd7d17d
copy ssh key (add following password): ssh-copy-id root@vm02.jk
password: vm02.jk
then ssh login using: ssh root@vm02.jk

----

TODO:
- create ansible to configure ssh on fresh vm
- fix ca and services certs
- clean coredns db before running setup-coredns task
- add wg-quick as systemd service: systemctl enable wg-quick@vm02wg00private
-------
wg02

<!-- docker run \
  --name=nginx-proxy-manager \
  --rm \
  -p 80:80 \
  -p 443:443 \
  -p 8002:81 \
  -v /opt/n02/nginx-proxy-manager/data:/data \
  -v /opt/n02/nginx-proxy-manager/letsencrypt:/etc/letsencrypt \
  jc21/nginx-proxy-manager:latest
 -->

docker run \
  --name=nginx-proxy-manager \
  --rm \
  --network host \
  -v /opt/n02/nginx-proxy-manager/data:/data \
  -v /opt/n02/nginx-proxy-manager/letsencrypt:/etc/letsencrypt \
  jc21/nginx-proxy-manager:latest

default
Username: admin@example.com
Password: changeme

changed
Username: jontykantiwal@gmail.com
Password: jonty16117
----
docker run -d \
  --name wgdashboard \
  --rm \
  --network host \
  --restart unless-stopped \
  --cap-add NET_ADMIN \
  -v /etc/wireguard:/etc/wireguard \
  -v /opt/WGDashboard:/data \
  -e "global_dns=your_dns_server_ip" \
  -e "public_ip=your_public_ip" \
  -e "tz=your_timezone" \
  donaldzou/wgdashboard:latest
-----
  docker run -d \
  --name coredns \
  --rm \
  --network host \
  --restart unless-stopped \
  -v /etc/coredns:/etc/coredns \
  coredns/coredns:latest \
  -conf /etc/coredns/Corefile


----
scp /home/jasforum/Downloads/vm02wg00private.conf root@192.168.178.100:/etc/wireguard/
chmod 600 /etc/wireguard/vm02wg00private.conf
wg-quick up vm02wg00private
systemctl enable wg-quick@vm02wg00private
------------
docker run --name nginx-rp \
  --dns=10.0.0.1 \
  -p 81:81 \
  -p 81:81 \
  -p 81:81 \
  nginx
------
docker run -d \
  --name nginx-rp \
  --restart always \
  --network proxy_net \
  -p 5080:80 \
  -p 5081:81 \
  -p 5443:443 \
  -e INITIAL_ADMIN_EMAIL="jontykantiwal@gmail.com" \
  -e INITIAL_ADMIN_PASSWORD="jonty16117" \
  -v /opt/nginx-rp/data:/data \
  -v /opt/nginx-rp/letsencrypt:/etc/letsencrypt \
  jc21/nginx-proxy-manager:latest
-------------
# Backup netbird_zdb_data
docker run --rm -v netbird_zdb_data:/data -v /root/backups:/backup alpine \
  tar czf /backup/netbird_zdb_data.tar.gz -C /data .

# Backup netbird_management
docker run --rm -v netbird_management:/data -v /root/backups:/backup alpine \
  tar czf /backup/netbird_management.tar.gz -C /data .

# Backup netbird_caddy_data
docker run --rm -v netbird_caddy_data:/data -v /root/backups:/backup alpine \
  tar czf /backup/netbird_caddy_data.tar.gz -C /data .

# Backup netbird_zitadel_certs
docker run --rm -v netbird_zitadel_certs:/data -v /root/backups:/backup alpine \
  tar czf /backup/netbird_zitadel_certs.tar.gz -C /data .

# Backup other files
tar czf /root/backups/netbird_configs.tar.gz \
  Caddyfile dashboard.env relay.env management.json turnserver.conf zitadel.env machinekey
--------------
docker run --rm -v netbird_zdb_data:/data -v /root/backups:/backup alpine sh -c "cd /data && tar xzf /backup/netbird_zdb_data.tar.gz"

# Restore netbird_zdb_data
docker run --rm -v netbird_zdb_data:/data -v /root/backups:/backup alpine \
  sh -c "cd /data && /backup/netbird_zdb_data.tar.gz"

# Restore netbird_management
docker run --rm -v netbird_management:/data -v /root/backups:/backup alpine \
  sh -c "cd /data && /backup/netbird_management.tar.gz"

# Restore netbird_caddy_data
docker run --rm -v netbird_caddy_data:/data -v /root/backups:/backup alpine \
  sh -c "cd /data && /backup/netbird_caddy_data.tar.gz"

# Restore netbird_zitadel_certs
docker run --rm -v netbird_zitadel_certs:/data -v /root/backups:/backup alpine \
  sh -c "cd /data && /backup/netbird_zitadel_certs.tar.gz"

# Restore other files
tar xvf /root/backups/netbird_configs.tar.gz \
  Caddyfile dashboard.env relay.env management.json turnserver.conf zitadel.env machinekey
------------
