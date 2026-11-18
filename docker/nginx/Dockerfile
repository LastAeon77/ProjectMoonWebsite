# The second stage
# Copy React static files and start nginx
FROM nginx:stable-alpine
RUN rm /etc/nginx/conf.d/*
CMD ["nginx", "-g", "daemon off;"] 