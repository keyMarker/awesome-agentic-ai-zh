# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "requests>=2.34.2",
# ]
# ///
import requests

#response = requests.get("https://api.github.com/users/torvalds")
response = requests.get("https://api.github.com/users/keymarker")
data = response.json()
followers_count = data['followers']
print(f"User has {followers_count} followers on GitHub.")

