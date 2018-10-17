import os

import pybridge
from pybridge import ApiClient
from pybridge.api import DefaultApi
from pybridge.configuration import Configuration
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


config = Configuration()
config.api_key['client_id'] = os.environ['BRIDGE_ID']
config.api_key['client_secret'] = os.environ['BRIDGE_SECRET']
client = ApiClient(config)
client.set_default_header('Bankin-Version', '2018-06-15')
client.set_default_header('default_headers', 'pybridge Client' + pybridge.__version__)
client.set_default_header('Accept', '*/*')
api = DefaultApi(client)

# api.delete_all_users()

user = ("new_user@gmail.com", '0123456789')

# print(api.create_user(*user, empty_body={}))

authenticated = api.authenticate_user(*user, empty_body={})

access_token = authenticated.access_token

config.api_key['authorization'] = access_token
config.api_key_prefix['authorization']= 'Bearer'

print(api.connect())

# do the connect,
# redirected to the /redirect url
# e.g. http://localhost:5000/redirect?item_id=2384385&user_uuid=094b4d5e-d15a-4cb6-b98e-23757d417b03

print(api.get_accounts())
print(api.get_account(12655088))
