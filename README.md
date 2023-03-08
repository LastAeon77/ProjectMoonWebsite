# ProjectMoonWebsite

You can visit website at: https://malcute.aeonmoon.page/

An example API: https://malcute.aeonmoon.page/api/lor/deck

A full-stack website with Frontend and backend configuration. Note that the secret key for Django is not included, so the user must make it themselves.

The projects work like this:
# Frontend
The frontend is Next.js, written using typescript. It's main job is to digest the information from the backend by calling APIs and using the data.
# Backend
The backend is Django, written using Python. There are several apps inside and models for the game Limbus and Library of Ruina. 
It provides API for the frontend in Next.js, and also my discord bot which can be found in https://github.com/LastAeon77/LibraryOfRuinaBot.
# Database
The database used is postgreSQL, where django mostly interact with it without needing direct SQL query or interface.
# Nginx
Nginx provides a service to redirect user to django or next.js as needed. If you do /api or /admin, it goes straight to backend (Django), otherwise it goes to frontend
# Certbot
Using code from: https://github.com/wmnnd/nginx-certbot, we have a script to initially start our certbot, which will then call a bash to certbot with letsencrypt every
12 hours for new certification to allow usage of https.

# Deployment
The website is deployed on digitalOcean linux server. Note that for frontend, only the build file is uploaded so that we do not need to build in the server as that would
be too expensive.
