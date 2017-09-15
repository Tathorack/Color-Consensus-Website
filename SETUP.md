### Set up virtual environment and install requirements

```bash
virtualenv -p python3 venv_flask
venv_flask/bin/pip install -r requirements.txt
echo "virtual environment setup"
cd flaskfiles/static/
npm install
echo "front-end packages installed"
```
### Set environment variables
```bash
export FLASKAPP_CONFIG
export GOOGLE_SEARCH_API
export GOOGLE_SEARCH_CSE
```
If using with Philips Hue
```bash
export BRIDGE_IP
export HUE_USER
```

### Raspberry Pi dependencies
```bash
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install \
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

sudo apt-get install \
libtiff5-dev

sudo pip3 install uwsgi
```
