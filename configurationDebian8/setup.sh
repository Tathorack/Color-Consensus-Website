#!/usr/bin/env bash

apt-get install virtualenv python3-dev nginx-full
pip3 install uwsgi

rm /etc/nginx/sites-enabled/*.conf
cp rhys.miad.edu.conf /etc/nginx/sites-enabled/rhys.miad.edu.conf
systemctl enable nginx
systemctl reload nginx
systemctl status nginx.service

mkdir -p /etc/uwsgi/vassals
cp emperor.ini /etc/uwsgi/emperor.ini
cp uwsgi.service /lib/systemd/system/uwsgi.service
cp rhysprojectsite.ini /etc/uwsgi/vassals/rhysprojectsite.ini
systemctl enable uwsgi.service
systemctl start uwsgi
