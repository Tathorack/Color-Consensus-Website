
### Set up virtual environment and install requirements

```bash
virtualenv venv_flask
venv_flask/bin/pip install -r requirements.txt

cd flaskfiles/static/
npm install
```
### Install API keys for Google

Add the following environment variables
* GOOGLE_SEARCH_API
* GOOGLE_SEARCH_CSE

If using with Philips Hue
* BRIDGE_IP
* HUE_USER

### TODO
* add data analysis pages

Example SQL query
```sql
SELECT column5, COUNT(*)
FROM table1
GROUP BY column5
```
Example sqlalchemy query
```python
from sqlalchemy import func
session.query(Table.column, func.count(Table.column)).group_by(Table.column).all()
```
Example of using templating for javascript paths
```html
<script src="{{ url_for('static', filename='scripts.js') }}"></script>
```
