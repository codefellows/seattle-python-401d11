# Deploy a Flask Application to AWS

### In your project

1. Ensure your `requirements.txt` reflects any additional dependencies installed via `pipenv` for local development
    - `pipenv run pip freeze > requirements.txt`

### On AWS
_You can skip some of these steps if you already have the instances created._

1. Create a new EC2 instance.
     - Choose the Ubuntu Server 16.04 from the free tier
     - Continue to the the security group settings
     - Use a security group with access to SSH, HTTP, and POSTGRESQL 
        - For now, allow access from anywhere
     - When launching, create a new key pair and download it
     - Launch the instance

1. Set up a ssh configuration for the EC2 instance.
     - Move the downloaded key pair `.pem` file to `~/.ssh`
     - Change the permissions for the `.pem` file to remove public access

        ```bash
        $ chmod 400 ~/.ssh/(key name).pem
        ```

     - Create a `config` file in `~/.ssh` and add the EC2 instance as a Host.

        ```ini
        # config
        Host (your name for host)
            Hostname (EC2 public DNS)
            User ubuntu
            IdentityFile ~/.ssh/(key name).pem
        ```

### In your project

1. Connect to your EC2 instance.

    ```bash
    $ ssh (host name)
    ```

     - Accept the instance being added to known hosts

### On the EC2 instance

1. Update `apt-get`.

    ```bash
    $ sudo apt-get update
    ```

1. Install necessary packages from `apt-get`.

    ```bash
    $ sudo apt-get install nginx build-essential python3-pip -y
    ```

13. Clone project repo onto the instance.
    ```bash
    $ cd ~
    $ git clone (link to repo).git src
    ```
    
14. Install pip requirements for project.
    ```bash
    $ cd src
    $ pip3 install -r requirements.txt
    ```

    **DO NOT USE SUDO TO PIP INSTALL.**
    
#### Nginx Restart Fix
1. _NOTE: The following steps are a fix which allow us to successfully restart Nginx on the instance after updating the configuration files. Without this fix, a full reboot of the instance is required to successfully restart Nginx._
```bash
sudo mkdir /etc/systemd/system/nginx.service.d
sudo nano /etc/systemd/system/nginx.service.d/override.conf
```
Then add the following line to that file. Save and close.
```
[Service]
ExecStartPost=/bin/sleep 0.1
```
Then run:
```bash
sudo systemctl daemon-reload
```

### Configure Nginx
17. Replace the default `nginx` configuration file.

    ```bash
    $ sudo nano /etc/nginx/nginx.conf
    ```
    Delete the contents of this file and paste the below file:

    ```ini
    # nginx.conf
    user www-data;
    worker_processes 4;
    pid /var/run/nginx.pid;

    events {
        worker_connections 1024;
        # multi_accept on;
    }

    http {

        ##
        # Basic Settings
        ##

        sendfile on;
        tcp_nopush on;
        tcp_nodelay on;
        keepalive_timeout 65;
        types_hash_max_size 2048;
        # server_tokens off;

        server_names_hash_bucket_size 128;
        # server_name_in_redirect off;

        include /etc/nginx/mime.types;
        default_type application/octet-stream;

        ##
        # Logging Settings
        ##

        access_log /var/log/nginx/access.log;
        error_log /var/log/nginx/error.log;

        ##
        # Gzip Settings
        ##

        gzip on;
        gzip_disable "msie6";

        ##
        # Virtual Host Configs
        ##

        include /etc/nginx/conf.d/*.conf;
        include /etc/nginx/sites-enabled/*;
    }
    ```

1. Add a new, project-specific, configuration for your nginx server
    ```bash
    $ sudo nano /etc/nginx/conf.d/(project_name).conf
    ```
    Paste the below contents into this file, update with your project details, save and exit:
    ```ini
    # (project_name).conf
    upstream (project_name) {
        server 127.0.0.1:8000;
    }

    server {
        listen 80;

        server_name (EC2 public DNS);

        access_log  /home/ubuntu/.local/nginx.access.log;

        location / {
            proxy_set_header        Host $http_host;
            proxy_set_header        X-Real-IP $remote_addr;
            proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header        X-Forwarded-Proto $scheme;

            client_max_body_size    10m;
            client_body_buffer_size 128k;
            proxy_connect_timeout   60s;
            proxy_send_timeout      90s;
            proxy_read_timeout      90s;
            proxy_buffering         off;
            proxy_temp_file_write_size 64k;
            proxy_pass http://(project_name);
            proxy_redirect          off;
        }
    }
    ```

1. Validate your updated nginx configs:
    ```bash
    $ sudo nginx -t
    nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
    nginx: configuration file /etc/nginx/nginx.conf test is successful
    $
    ```

1. Check that `nginx` is working properly.
    ```bash
    $ sudo systemctl status nginx
    ```

     - If `nginx` is failing:
        ```bash
        $ sudo systemctl restart nginx 
        ```

        You can also check the error logs at `/var/log/nginx/error.log`.

1. Install `gunicorn` with `pip3`.
    ```bash
    $ pip3 install gunicorn python-dotenv
    ```

1. Create a `gunicorn` configuration file.
    ```bash
    $ sudo nano /etc/systemd/system/gunicorn.service
    ```

    ```ini
    # gunicorn.service
    [Unit]
    Description=(your description)
    After=network.target

    [Service]
    User=ubuntu
    Group=www-data
    EnvironmentFile=/home/ubuntu/src/.env
    WorkingDirectory=/home/ubuntu/src
    ExecStart=/home/ubuntu/.local/bin/gunicorn --access-logfile - -w 3 wsgi:app

    [Install]
    WantedBy=multi-user.target
    ```

1. Start up `gunicorn` and check that it is working properly.

    ```bash
    $ sudo systemctl enable gunicorn
    $ sudo systemctl start gunicorn
    $ sudo systemctl status gunicorn
    ```

## Check in!
Go check out your site on EC2! You should see the home page.


### Finish up - Run Migrations to your RDS instance
Update your `.env` file on EC2 and ensure that you have the following settings correctly configured
```dotenv
FLASK_APP=wsgi.py
FLASK_ENV=production
DATABASE_URL=postgres://<USERNAME>:<PASSWORD>@<HOST>/postgres
SECRET_KEY=1234  # Generate a secret random string of 16 or more characters
API_URL=https://....
```

Migrate database using `flask db upgrade` from the root of your project: `src/`


## Making updates!
1. Continue to develop your code locally, and ACP to GitHub.
1. SSH into your EC2 Instance and `git pull` from your repo.
1. Restart Gunicorn - `sudo systemctl restart gunicorn`.

_Note: You may need to process other steps as you progress, such as migrations to your database._

