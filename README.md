
### Set up virtual environment and install requirements

```bash
virtualenv venv_flask
venv_flask/bin/pip install -r requirements.txt

cd flaskfiles/static/
npm install
```
### Install API keys for Google
Select the config to use or leave empty for default
* FLASKAPP_CONFIG

Add the following environment variables
* GOOGLE_SEARCH_API
* GOOGLE_SEARCH_CSE

If using with Philips Hue
* BRIDGE_IP
* HUE_USER
