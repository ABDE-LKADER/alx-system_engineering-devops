# Puppet manifest to optimize Nginx for handling high request loads

# Manage the Nginx configuration file
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => "
worker_processes auto;

events {
    worker_connections 1024; # Adjust this based on your needs
}

http {
    server {
        listen 80;
        server_name localhost;

        location / {
            proxy_pass http://backend;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
  ",
  notify  => Service['nginx'], # Notify the Nginx service to restart if the config changes
}

# Ensure the Nginx service is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/nginx.conf'], # Restart service if the configuration file changes
}
