#This logs in and stores your ID Token, Access Token, and Refresh Token

import json
from pycognito import Cognito
from getpass import getpass

USER_POOL_ID = "us-west-2_LXw9Rf9qM"
CLIENT_ID = "3au5f4m5juu58qks62mcd89730"
USERNAME = "XXXXXXXXXXXX" #Replace with your login
PASSWORD = "XXXXXXXXXXXX" #Replace with your password

u = Cognito(USER_POOL_ID, CLIENT_ID, username=USERNAME)
u.authenticate(password=PASSWORD)

tokens = {
    'id_token': u.id_token,
    'access_token': u.access_token,
    'refresh_token': u.refresh_token,
}

with open('hydros_tokens.json', 'w') as f:
    json.dump(tokens, f, indent=2)

print("\nLogin successful! Tokens saved to hydros_tokens.json.")
