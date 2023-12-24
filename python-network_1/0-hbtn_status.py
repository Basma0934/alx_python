"""Writing a Python script that fetches https://alu-intranet.hbtn.io/status"""
import requests

request = requests.get('https://alu-intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode("utf-8")))