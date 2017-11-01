FROM nginx:1.9
MAINTAINER Nick Janetakis <nick.janetakis@gmail.com>

RUN rm /usr/share/nginx/html/*

COPY configs/nginx.conf /etc/nginx/nginx.conf
COPY configs/default.conf /etc/nginx/conf.d/default.conf
COPY configs/default.conf /etc/nginx/conf.d/timeout.conf

COPY certs/ssl-bundle.crt /etc/ssl/certs/ssl-bundle.crt
COPY certs/karnas.key /etc/ssl/private/karnas.key
COPY certs/dhparam.pem /etc/ssl/private/dhparam.pem

COPY docker-entrypoint /
RUN chmod +x /docker-entrypoint
ENTRYPOINT ["/docker-entrypoint"]

CMD ["nginx", "-g", "daemon off;"]
