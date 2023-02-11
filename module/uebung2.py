import requests
homepage = requests.get("https://uni-tuebingen.de")
print(homepage.text)
