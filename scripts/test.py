import os

from pybridge import ApiClient
from pybridge.api import DefaultApi
from pybridge.configuration import Configuration
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


config = Configuration()
config.api_key['client_id'] = os.environ['BRIDGE_ID']
config.api_key['client_secret'] = os.environ['BRIDGE_SECRET']
client = ApiClient(config)
client.default_headers['Bankin-Version'] = '2018-06-15'
api = DefaultApi(client)

api.delete_all_users()

print(api.create_user("user@bridgeapi.io", '0123456789'))
