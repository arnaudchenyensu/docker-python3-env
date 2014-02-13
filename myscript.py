import requests

r = requests.get('http://google.com')
print(r.status_code)
