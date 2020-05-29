from urllib.request import urlopen, Request
import gzip

request = Request('http://www.gmrit.org')
request.add_header('Accept-Encoding', 'gzip')   # Adding Request Headers
response = urlopen(request)

print('Request Headers: ')              # Printing Request Headers
print(request.header_items())

print('\nResponse Headers: ')           # Printing Response Headers
print(response.getheaders())

print('\nResponse Body Before Decoding: ')  # response body withot extracting
body = response.read()
print(body)

print('\nResponse body after Decoding')       # Response body after extraction
content = gzip.decompress(body)

print(content.decode('unicode_escape'))       # raw data to normal
