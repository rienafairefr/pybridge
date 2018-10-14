import os

from pybridge.api import BridgeClient, BridgeConfig, BridgeUserCredentials
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


config = BridgeConfig(os.environ['BRIDGE_ID'], os.environ['BRIDGE_SECRET'])
client = BridgeClient(config)

#client.delete_users()

credentials = BridgeUserCredentials(email='user@bridge.io', password='0123456789')

#client.create_user(credentials)
user = client.authenticate_user(credentials)

print(client.get_clients())



