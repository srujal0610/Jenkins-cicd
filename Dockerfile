# Use an official PHP with Apache image
FROM php:8.2-apache
WORKDIR /var/www/html/

RUN echo "starting to build the dockerfile"

RUN docker-php-ext-install mysqli pdo pdo_mysql

COPY . /var/www/html/

RUN ls -lah /var/www/html/

RUN chown -R www-data:www-data /var/www/html \
    && chmod -R 755 /var/www/html

RUN a2enmod rewrite

EXPOSE 80

CMD ["apache2-foreground"]

