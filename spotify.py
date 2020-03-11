# Dependencies and Setup
import numpy as np
import requests
import json
import time


url = "https://api.spotify.com/v1/audio-features/06AKEBrKUckW0KREUWRnvT"
headers = {'Accept': 'application/json', 'Content-Type' : 'application/json','Authorization': 'Bearer BQDo_QQrTMzeXflGzXGvJA0dkx3C0URuGLzn14FKNXBJ8-nekZ32n7-Prlsa8wOzfLB06M0sZq3OdA7nOfeY6eMX45pAiISt_vYH0rX8KgCEvC0R4XUQkBVO0DmKsAJNQ4LDNU5s8_8'}


req = requests.get(url, headers=headers)
jreq = req.json()
print(jreq)

