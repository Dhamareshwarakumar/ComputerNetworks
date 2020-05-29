import requests


response = requests.get('https://www.google.com')

print('status: '+str(response.status_code))
print(response.text)
