import requests

# requesting data from website
r=requests.get("https://www.ibm.com")
# printing the status code
print(r.status_code)
print(r.headers)
# print(r.text)
print(r.text[:100])

#If status code is 200, then the request was successful
#If status code is 404, then the requested resource was not found
#If status code is 500, then there was an internal server error


