import requests

print("Version of requests is ", requests.__version__)

homepage = requests.get("https://www.google.com")

raw_url = "https://raw.githubusercontent.com/HolaClubSandwich/CMPUT404_Lab1/master/lab1.py"

code = requests.get(raw_url, stream=True)

with open("lab1_dowload.py", "wb") as file:
    file.write(code.content)

print(code.text)