import urllib.request
from urllib.request import Request, urlopen


request = Request('http://www.stepcone.gmrit.org')
request.add_header('Accept-Language', 'sv')
response = urlopen(request)

print("Request Headers are....")
for header in request.header_items():
    print(header)
print()

print('Response headers are...')
for header in response.getheaders():
    print(header)
