FROM php:7.4-cli

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    autoconf \
    pkg-config \
    curl \
    unzip \
    git \
    openssh-client \
    libgrpc-dev \
    && pecl install grpc \
    && docker-php-ext-enable grpc \
    && rm -rf /var/lib/apt/lists/*

# Install PHP extensions via docker-php-ext-install
RUN docker-php-ext-install curl mbstring xml zip intl

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
