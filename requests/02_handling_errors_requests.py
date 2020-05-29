import requests
# from urllib.error import HTTPError
from requests.exceptions import HTTPError

try:
    response = requests.get('http://www.gmrit.org/hsdvhjdvsh')
    response.raise_for_status()
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)
