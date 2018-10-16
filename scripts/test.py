import os

import pybridge
from pybridge import ApiClient
from pybridge.api import DefaultApi
from pybridge.configuration import Configuration
from dotenv import load_dotenv, find_dotenv
import http
http.client.HTTPConnection.debuglevel=5

load_dotenv(find_dotenv())


config = Configuration()
config.api_key['client_id'] = os.environ['BRIDGE_ID']
config.api_key['client_secret'] = os.environ['BRIDGE_SECRET']
client = ApiClient(config)
client.set_default_header('Bankin-Version', '2018-06-15')
client.set_default_header('default_headers', 'pybridge Client' + pybridge.__version__)
client.set_default_header('Accept', '*/*')
api = DefaultApi(client)

api.delete_all_users()

print(api.create_user("new_user@gmail.com", '0123456789', empty_body={}))
