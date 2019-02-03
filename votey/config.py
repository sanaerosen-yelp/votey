import os

class Default:
  SLACK_API_TOKEN = os.environ.get('SLACK_API_TOKEN')
  SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
  CLIENT_ID = os.environ.get('CLIENT_ID')
  CLIENT_SECRET = os.environ.get('CLIENT_SECRET')