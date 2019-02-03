import hashlib
import os
from datetime import datetime, timedelta

import bridge
from bridge import ApiClient
from bridge.bridge_api import BridgeApi
from bridge.configuration import Configuration
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


config = Configuration()
config.api_key['client_id'] = os.environ['BRIDGE_ID']
config.api_key['client_secret'] = os.environ['BRIDGE_SECRET']
client = ApiClient(config)
client.set_default_header('Bankin-Version', '2018-06-15')
client.set_default_header('default_headers', 'pybridge Client' + pybridge.__version__)
client.set_default_header('Accept', '*/*')
api = BridgeApi(client)

# api.delete_all_users()

user = (os.environ['BRIDGE_USERNAME'], os.environ['BRIDGE_PASSWORD'])

# print(api.create_user(*user, empty_body={}))

authenticated = api.authenticate_user(*user, empty_body={})

access_token = authenticated.access_token

config.api_key['authorization'] = access_token
config.api_key_prefix['authorization']= 'Bearer'

# print(api.connect())

# do the connect,
# redirected to the /redirect url
# e.g. http://localhost:5000/redirect?item_id=2384385&user_uuid=094b4d5e-d15a-4cb6-b98e-23757d417b03

# print(api.get_accounts())
# print(api.get_account(12655088))

print(api.get_updated_transactions(since=(datetime.utcnow() - timedelta(days=5)).isoformat()))

# print(api.get_transaction(38000036919216))

