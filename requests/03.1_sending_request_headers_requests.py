import requests

headers = {
    'Accept-Language': 'Telu'
}
response = requests.get('http://www.stepcone.gmrit.org', headers=headers)

print('Response Headers....')
print(response.headers)
