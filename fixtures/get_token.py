from pytest import fixture


@fixture
def get_base_url_ELK():
    return "https://demo-passport.etpgpb.ru/api/v2"


@fixture
def get_base_url_HubAdmin():
    return


@fixture
def get_headers(get_auth_token):
    return {
        'accept': 'application/json',
        'Authorization' : get_auth_token
    }

import requests
@fixture
def get_auth_token():
    url = "https://id-test.etpgpb.ru/auth/realms/master/protocol/openid-connect/token"

    payload = 'grant_type=client_credentials&client_id=hub-admin-service&client_secret=a42f090b-cda5-4b2c-86ab-aa52c42fb061'
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return f"Bearer {response.json()["access_token"]}"