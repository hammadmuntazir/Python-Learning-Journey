import requests

Person={"name":"Hammad","Age":20}

# r_get=requests.get('https://www.google.com/search?q=kitab+al+irshad+islam+mobility&oq=&gs_lcrp=EgZjaHJvbWUqCQgCECMYJxjqAjIJCAAQIxgnGOoCMgkIARAjGCcY6gIyCQgCECMYJxjqAjIJCAMQIxgnGOoCMgkIBBAjGCcY6gIyCQgFECMYJxjqAjIJCAYQIxgnGOoCMgkIBxAjGCcY6gLSAQg2MTU4ajBqN6gCCLACAfEFuWT1Q5rHu2DxBblk9UOax7tg&sourceid=chrome&ie=UTF-8')
# print(r_get.url)
# print(r_get.request.body)
r_post=requests.get("https://httpbin.org/post",data=Person)
print(r_post.url)
print(r_post.request.body)