# Use an official OpenSSH image as a parent image
FROM ubuntu:latest

# # Install OpenSSH server and any other necessary packages
# RUN apt-get update && \
#     apt-get install -y openssh-server && \
#     apt-get install -y sudo && \
#     rm -rf /var/lib/apt/lists/*

# Install OpenSSH server and any other necessary packages
RUN apt-get update && \
    apt-get install -y openssh-server && \
    apt-get install -y sudo

# Create a user for GitLab SSH access
RUN useradd -m -d /home/gitlab -s /bin/bash gitlab && \
    echo "gitlab:gitlab" | chpasswd && \
    usermod -aG sudo gitlab

# Configure SSH
RUN mkdir -p /var/run/sshd && \
    echo 'PermitRootLogin prohibit-password' >> /etc/ssh/sshd_config && \
    echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config

# # Copy the authorized_keys file for GitLab
# COPY authorized_keys /home/gitlab/.ssh/authorized_keys
# RUN chown -R gitlab:gitlab /home/gitlab/.ssh && \
#     chmod 700 /home/gitlab/.ssh && \
#     chmod 600 /home/gitlab/.ssh/authorized_keys

# # Expose the SSH port
# EXPOSE 2424

# Copy the entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]
