# The first stage
# Build React static files
FROM node:18-alpine as build

WORKDIR /app/frontend
RUN npm install --global pm2
RUN npm install --global next
COPY ./frontend/package.json ./
COPY ./frontend/package-lock.json ./
COPY ./frontend/ ./
EXPOSE 3000
USER node
CMD [ "pm2-runtime", "npm", "--", "start" ]
