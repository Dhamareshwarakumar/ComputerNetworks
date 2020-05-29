import urllib.request

response = urllib.request.urlopen('http://www.stepcone.gmrit.org')

print(response.getheaders())

for header in response.getheaders():
    print(header)
