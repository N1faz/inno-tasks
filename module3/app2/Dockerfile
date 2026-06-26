FROM node:18 AS build
WORKDIR /app
COPY package.json .
RUN npm install && npm cache clean --force
COPY . .
RUN npm run build

FROM nginx:alpine
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
COPY --from=build /app/build /usr/share/nginx/html
RUN mkdir -p /var/cache/nginx /var/log/nginx /tmp/nginx && \
    mkdir -p /var/tmp/nginx/client_body /var/tmp/nginx/proxy /var/tmp/nginx/fastcgi && \
    mkdir -p /var/tmp/nginx/uwsgi /var/tmp/nginx/scgi && \
    chown -R appuser:appgroup /var/cache/nginx /var/log/nginx /tmp/nginx && \
    chown -R appuser:appgroup /var/tmp/nginx && \
    chown -R appuser:appgroup /usr/share/nginx/html && \
    chown -R appuser:appgroup /etc/nginx
RUN rm -rf /docker-entrypoint.d /docker-entrypoint.sh
# Копируем конфиги (если есть)
COPY nginx.conf /etc/nginx/nginx.conf

# Меняем владельца на appuser
RUN chown -R appuser:appgroup /etc/nginx/conf.d /etc/nginx/nginx.conf

USER appuser
EXPOSE 8080
HEALTHCHECK --interval=20s --timeout=4s --start-period=5s --retries=3 CMD wget http://localhost:8080 || exit 1
ENTRYPOINT ["/usr/sbin/nginx"]
CMD ["-g", "daemon off;"]
