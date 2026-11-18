# docker/backend/Dockerfile

FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ADD ./backend/requirements.txt /app/backend/

# gunicorn is pinned in requirements.txt; --no-cache-dir keeps the image (and the
# droplet's memory/disk use during the build) small.
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r backend/requirements.txt

ADD ./docker /app/docker
ADD ./backend /app/backend
