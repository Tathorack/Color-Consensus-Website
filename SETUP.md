
### Set up virtual environment and install requirements

```bash
virtualenv venv_flask
venv_flask/bin/pip install -r requirements.txt
echo "virtual environment setup"
cd flaskfiles/static/
npm install
echo "front-end packages installed"
```
### Install API keys for Google
move api_keys.py to flaskfiles/extensions


export FLASKAPP_ENV='test'


sudo apt-get update
sudo apt-get upgrade

sudo apt-get install \
libfreetype6-dev \
libjpeg-dev \
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

sudo apt-get install \
libtiff5-dev

sudo pip3 install uwsgi
