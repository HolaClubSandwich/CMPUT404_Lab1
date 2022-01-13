import requests

print("Version of requests is ", requests.__version__)

homepage = requests.get("https://www.google.com")

