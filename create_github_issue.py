import requests
import sys

token = sys.argv[1]
message = sys.argv[2]
repo = sys.argv[3]
headers = {"Authorization": "token {0}".format(token)}
payload = {"title": message}
requests.post(
    url='https://api.github.com/repos/arbor-test/{0}/issues'.format(repo),
    headers=headers, data=payload)
