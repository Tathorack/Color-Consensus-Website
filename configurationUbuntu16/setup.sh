#!/usr/bin/env bash

apt-get install virtualenv python3-dev python3-pip nginx-full npm
pip3 install uwsgi

rm /etc/nginx/sites-enabled/*.conf
cp thesis-web.conf /etc/nginx/sites-enabled/thesis-web.conf
systemctl enable nginx
systemctl reload nginx
systemctl status nginx

mkdir -p /etc/uwsgi/vassals
cp emperor.ini /etc/uwsgi/emperor.ini
cp uwsgi.service /lib/systemd/system/uwsgi.service
cp thesis-web.ini /etc/uwsgi/vassals/thesis-web.ini
systemctl enable uwsgi.service
systemctl start uwsgi
systemctl status uwsgi

mkdir -p /var/log/uwsgi
chown www-data:www-data /var/log/uwsgi

echo 'Complete'
