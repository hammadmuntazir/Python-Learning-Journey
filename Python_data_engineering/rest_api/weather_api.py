import requests

response = requests.get("https://wttr.in/Karachi?format=%t")

if response.status_code ==200:
    print("Current temperature in Karachi :",response.text)