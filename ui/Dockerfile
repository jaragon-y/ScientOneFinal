# nginx state for serving content
FROM nginx:alpine
#copiando build
COPY --chown=101:101 /dist/ui /usr/share/nginx/html/
ENTRYPOINT ["nginx", "-g", "daemon off;"]
