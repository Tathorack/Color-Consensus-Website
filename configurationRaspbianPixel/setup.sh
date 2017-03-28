#!/usr/bin/env bash

apt-get update
apt-get upgrade

apt-get install \
libfreetype6-dev \
libjpeg8-dev \
liblcms2-dev \
libwebp-dev \
nginx \
npm \
python3-dev \
python3-pip \
python3-tk \
tcl8.6-dev \
tk8.6-dev \
virtualenv \
zlib1g-dev

apt-get install \
libtiff5-dev

pip3 install uwsgi

systemctl enable nginx
rm /etc/nginx/sites-enabled/*.conf
cp rhys.miad.edu.conf /etc/nginx/sites-enabled/rhys.miad.edu.conf
systemctl reload nginx
systemctl status nginx.service

mkdir -p /etc/uwsgi/vassals
cp emperor.ini /etc/uwsgi/emperor.ini
cp uwsgi.service /lib/systemd/system/uwsgi.service
cp rhysThesisLights.ini /etc/uwsgi/vassals/rhysThesisLights.ini
systemctl enable uwsgi.service
systemctl start uwsgi
systemctl status nginx.service

mkdir /var/log/uwsgi
chown www-data:www-data /var/log/uwsgi
