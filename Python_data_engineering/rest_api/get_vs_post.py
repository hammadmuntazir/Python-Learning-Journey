import requests

payload = {"name": "Joseph", "id": "123"}

# GET REQUEST
r_get = requests.get("https://httpbin.org/get", params=payload)
print("GET URL:", r_get.url)
print("GET Body:", r_get.request.body)  # None (body nahi hai)

print("-" * 50)

# POST REQUEST  
r_post = requests.post("https://httpbin.org/post", data=payload)
print("POST URL:", r_post.url)  # Parameters nahi dikhte
print("POST Body:", r_post.request.body)  # Data dikhta hai

r = requests.get("https://example.com")

# r.status_code    # Status code (200, 404, etc)
# r.headers        # Response headers (dictionary)
# r.text           # Response body as text
# r.url            # URL jo request ki thi
# r.encoding       # Encoding type (utf-8, etc)

# # For JSON responses
# r.json()         # Response as Python dictionary