import requests

response = requests.get("https://api.robinhood.com/fundamentals/ETC")
print(response.status_code)