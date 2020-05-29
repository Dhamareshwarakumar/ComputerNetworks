import urllib.request
from urllib.error import HTTPError


try:
    response = urllib.request.urlopen('http://www.gmrit.org/hjavjdhgf')
except HTTPError as e:
    print('status: '+str(e.code))
    print('reason: '+str(e.reason))
    print('url: '+str(e.url))
except Exception as e:
    print('Error: ', e)
