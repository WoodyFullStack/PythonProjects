import requests

response = requests.get("https://api.github.com/users/WoodyFullStack/repos")

print(type(response.json()[0]))
for proj in range(0, len(response.json())):
    print(f" Project: {response.json()[proj].get('name')} link - {response.json()[proj].get('url')} ")
