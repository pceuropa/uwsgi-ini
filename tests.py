"""
File: tests.py
Authors: Rafal Marguzewicz
Emails: info@pceuropa.net
Github: https://github.com/pceuropa/uwsgi-ini
Description: pytest to check urls of API based on https://github.com/pceuropa/testing-rest-api
"""

from urllib.request import urlopen, Request

host = f"http://127.0.0.1:8000"
endpoint = '/'


def headers():
    """
    Posibility adding authorization token to header of  request
    """
    return {'Authorization': 'token_secure'}


def request(endpoint_url: str=''):
    """If post method:
    data = str(json.dumps({'data': 'post_data'})).encode('utf-8')
    return Request(f"{host}/{endpoint_url}", data=data, headers=headers())
    """
    return Request(f"{host}/{endpoint_url}", headers=headers())


def test_endpoint_200():
    """
    Response 200
    """
    req = request(f"{endpoint}")
    assert 200 == urlopen(req).getcode()
