import requests
url = "https://192.168.0.21/command-api"

commands = open("eth3.json","r")

r = requests.post(url, auth=('arista', 'aristaetax'), data = commands, verify = False)

print(r.text)