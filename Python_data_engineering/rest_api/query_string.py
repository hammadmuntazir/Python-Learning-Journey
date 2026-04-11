# GET Request with Query String (Parameters):
# Query String kya hai?
# URL mein ? ke baad jo data hota hai
# https://example.com/get?name=Joseph&id=123

import requests

payload = {'name': 'hammad', 'id': 123}
# Get request with query string
r=requests.get("https://httpbin.org/get", params=payload)
# print(r.url)
print(r.status_code)
data=r.json()
print(data['arge'])