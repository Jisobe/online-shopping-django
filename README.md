## Actions to start site
- start postgres in terminal
- clone repository and cd into it
- create and start venv 
  `python -m venv venv`
  `source venv/bin/activate`
- install requirements
  `pip install -r requirements.txt`
- create the database
  `createdb craigslist_db`
- migrate
  `python manage.py migrate`
- load data
  `python manage.py loaddata craigslist2.json`
- start server
  `python manage.py runserver`
- load main page
  - type `/categories` after port in browser bar
