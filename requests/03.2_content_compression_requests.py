import requests


headers = {
    'Accept-Encoding': 'gzip'
}

response = requests.get('http://www.gmrit.org', headers=headers)

print('Response Headers are: ')
print(response.headers)

print('\nResponse body After Decoding')
print(response.text)
