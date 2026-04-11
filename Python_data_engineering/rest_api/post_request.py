import requests

# Ye data tum bhejna chahte ho
payload = {
    "name": "Joseph",
    "id": "123"
}

# POST request
r = requests.post("https://httpbin.org/post", data=payload)

# Dekho URL (isme parameters nahi dikhte)
print(r.url)  
# Output: https://httpbin.org/post

# Body mein data gaya hai
print(r.text)

# JSON format mein dekho
data = r.json()
print(data['form'])  # {'name': 'Joseph', 'id': '123'}