import requests as req


url = 'http://127.0.0.1/test'
headers = {'Authorization': 'Basic YWRtaW46YWRtaW4='}

res = req.post(url, headers=headers)
print(res.text)
