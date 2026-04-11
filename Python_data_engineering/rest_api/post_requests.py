import requests

new_post={
    "title":"My First Post",
    "body":"This is the body of my first post.",
    "userId":1
}

response=requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)

if response.status_code == 200:
    print("Post created successfully!")
    print("Response JSON:", response.json())
else:
    print("Failed to create post. Status code:", response.status_code)