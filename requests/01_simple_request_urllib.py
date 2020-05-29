import urllib.request

response = urllib.request.urlopen('https://www.google.com')

print('status: '+str(response.status))
print(response.readline())
