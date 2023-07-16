#!/usr/bin/env bash
# setup web static files
sudo apt-get update > /dev/null
sudo apt-get -y install nginx > /dev/null

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

cd /data/web_static/releases/test/ ; echo "HBNB Static files" > sudo index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown ubuntu:ubuntu /data/ -hR

sudo sed -i '22i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-enabled/default

sudo service nginx restart
