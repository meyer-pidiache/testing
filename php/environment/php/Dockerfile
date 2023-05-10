# ./php/Dockerfile
FROM php:8-fpm-buster

ARG TIMEZONE

# Install PHP extensions Type docker-php-ext-install to see available extensions
RUN docker-php-ext-install pdo pdo_mysql 

RUN apt-get update && apt-get install -y git unzip

# Install PHP extensions Type docker-php-ext-install to see available extensions
RUN docker-php-ext-install pdo pdo_mysql

# Get latest Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Set timezone
RUN ln -snf /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && echo ${TIMEZONE} > /etc/timezone
RUN printf '[PHP]\ndate.timezone = "%s"\n', ${TIMEZONE} > /usr/local/etc/php/conf.d/tzone.ini
RUN "date"

# Set working directory
WORKDIR /var/www
