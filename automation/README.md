## Example run
ansible-playbook playbooks/update-eigenbox.yaml

## Folder structure
.
├── ansible.cfg
├── creds
├── files
├── inventory
│   ├── group_vars
│   │   ├── all.yaml
│   │   ├── clients.yaml
│   │   ├── eigenbox
│   │   └── eigenbox.yaml
│   └── hosts.yaml
├── playbooks
│   ├── setup-eigenbox.yaml
│   ├── teardown-eigenbox.yaml
│   └── update-eigenbox.yaml
├── README.md
├── roles
│   ├── base
│   │   └── tasks
│   ├── ddns
│   │   └── tasks
│   ├── dns
│   │   └── tasks
│   ├── docs_site
│   │   ├── files
│   │   ├── tasks
│   │   └── templates
│   ├── headscale
│   │   └── tasks
│   ├── monitoring
│   │   └── tasks
│   ├── network
│   │   └── tasks
│   ├── services
│   │   └── tasks
│   ├── storage
│   │   └── tasks
│   └── systemd
│       └── tasks
├── templates
└── vars
    ├── main.yaml
    └── secrets.yaml

## Setup project
- ./setup-project.sh
- source ./ansible-venv/bin/activate.fish

## Create new ansible role
ansible-galaxy init roles/role_name

#### Setup wg-server
- ping: ansible wg-server -m ping
- run playbook: ansible-playbook playbook.yml

## Ansible vault encrypt
find inventory/host_vars -type f -exec ansible-vault encrypt --vault-password-file ~/creds {} \;

## Ansible vault decrypt
find inventory/host_vars -type f -exec ansible-vault decrypt --vault-password-file ~/.ansible_vault_pass.txt {} \;
