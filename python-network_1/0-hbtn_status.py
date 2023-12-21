"""Writing a Python script that fetches https://alu-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    request = urllib.request.Request("https://intranet.hbtn.io/status")
with urllib.request.urlopen(request) as response:
html = response.read()
