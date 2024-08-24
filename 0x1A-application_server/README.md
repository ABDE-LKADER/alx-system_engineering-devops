# 0x1A. Application Server

## Overview

This project involves setting up and configuring an application server to serve dynamic content alongside a web server. The goal is to integrate Gunicorn as the WSGI server with Nginx as the reverse proxy, while ensuring the application is robust and scalable.

## Deadline

- **Start Date:** Aug 19, 2024, 4:00 AM
- **End Date:** Aug 25, 2024, 4:00 AM

## Auto QA Review

- **Mandatory:** 0.0/15
- **Optional:** 0.0/9
- **Overall:** 0.0%

## Concepts

For this project, you are expected to understand and apply the following concepts:

- Web Server
- Server
- Web stack debugging

## Background Context

Your web infrastructure is already serving static web pages via Nginx. In this project, you will extend your infrastructure to include an application server. You will integrate this with Nginx to serve dynamic content for your Airbnb clone project.

## Resources

Read or watch:

- [Application server vs web server](#)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](#)
- [Running Gunicorn](#)
- [Upstart documentation](#)

## Requirements

### General

- A `README.md` file is mandatory at the root of the project folder.
- All Python-related tasks must use Python 3.
- All config files must have comments.

### Bash Scripts

- All files will be interpreted on Ubuntu 16.04 LTS.
- All files should end with a new line.
- All Bash script files must be executable.
- Scripts must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without errors.
- The first line of all Bash scripts should be `#!/usr/bin/env bash`.
- The second line should be a comment explaining the script's purpose.

### Your Servers

| Name          | Username | IP Address         | State   |
|---------------|----------|--------------------|---------|
| 269784-web-01 | ubuntu   | 3.83.253.159       | running |
| 269784-web-02 | ubuntu   | 54.165.179.51      | running |
| 269784-lb-01  | ubuntu   | 35.174.209.104     | running |

## Tasks

### 0. Set up development with Python (Mandatory)

1. Ensure task #3 of your SSH project is completed for `web-01`.
2. Install `net-tools` on your server: `sudo apt install -y net-tools`.
3. Clone your `AirBnB_clone_v2` repository on `web-01`.
4. Configure `web_flask/0-hello_route.py` to serve content from the route `/airbnb-onepage/` on port 5000.

### 1. Set up production with Gunicorn (Mandatory)

1. Install Gunicorn and required libraries.
2. Configure Gunicorn to serve the Flask application on port 5000.
3. Ensure no other process is using port 6000.

### 2. Serve a page with Nginx (Mandatory)

1. Configure Nginx to serve the page at `/airbnb-onepage/` both locally and on the public IP on port 80.
2. Proxy requests to the process listening on port 5000.
3. Include the Nginx config file as `2-app_server-nginx_config`.

### 3. Add a route with query parameters (Mandatory)

1. Configure Nginx to proxy requests to `/airbnb-dynamic/number_odd_or_even/(any integer)` to a Gunicorn instance on port 5001.
2. Include the Nginx config file as `3-app_server-nginx_config`.

### 4. Serve your API (Mandatory)

1. Clone your `AirBnB_clone_v3` repository.
2. Configure Nginx to route `/api/` to a Gunicorn instance on port 5002.
3. Upload the Nginx config file as `4-app_server-nginx_config`.

### 5. Serve your AirBnB clone (Mandatory)

1. Clone your `AirBnB_clone_v4` repository.
2. Configure Gunicorn to serve content from `web_dynamic/2-hbnb.py` on port 5003.
3. Set up Nginx to serve static assets and the page from port 5003.
4. Upload the Nginx config as `5-app_server-nginx_config`.

### 6. Deploy it! (Advanced)

1. Write a `systemd` script to start Gunicorn with 3 worker processes.
2. Ensure it logs errors and access to `/tmp/airbnb-error.log` and `/tmp/airbnb-access.log`.
3. Upload the `gunicorn.service` file.

### 7. No service interruption (Advanced)

1. Write a Bash script to reload Gunicorn gracefully to avoid service interruptions during updates.

## Repository

- **GitHub Repository:** [alx-system_engineering-devops](https://github.com/alx-system_engineering-devops)
- **Directory:** `0x1A-application_server`
