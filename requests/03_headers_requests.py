import requests

response = requests.get('http://www.stepcone.gmrit.org')

print(response.headers)

print(response.headers['last-modified'])
