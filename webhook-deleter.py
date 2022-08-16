# imports 
import time
import os
try:
    import requests
except:
    os.system("python3 -m pip install requests")
    import requests

print("Simple webhook deleter")
webhook = str(input("Webhook: "))
try:
    requests.delete(webhook)
except:
    pass
print("Succesfully deleted webhook IF exists")
os.system("pause")