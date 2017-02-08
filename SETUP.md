
### Set up virtual environment and install requirements

```bash
virtualenv venv_flask
venv_flask/bin/pip install flaskfiles/extensions/image_colors-*
venv_flask/bin/pip install flaskfiles/extensions/image_search_colors-*
venv_flask/bin/pip install -r requirements.txt
echo "virtual environment setup"
cd flaskfiles/static/
npm install
echo "front-end packages installed"
```
### Install API keys for Google
move api_keys.py to flaskfiles/extensions
