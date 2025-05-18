#!/bin/bash

# Ensure the SSH directory exists
mkdir -p /var/run/sshd

sleep infinity

# Start the SSH server
/usr/sbin/sshd -D
