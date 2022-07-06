import requests 
import json
import os

directory = r"/home/superforce/lab/api-tecnofit-report/panda/report"

data = {'grant_type':"client_credentials", 
        'resource':"https://graph.microsoft.com", 
        'client_id':'e8d849c6-d00b-4c39-bcd3-c953aad56d04', 
        'client_secret':'749fa3cf-2a16-41cb-a5e9-8a39cb18afbc'} 

URL = "https://login.windows.net/AA7B6120B5A9AD93!1499/oauth2/token?api-version=1.0"
r = requests.post(url = URL, data = data) 
j = json.loads(r.text)
TOKEN = j["access_token"]

URL = "https://graph.microsoft.com/v1.0/users/relatorios@superforce.com.br/drive/root:/fotos/HouseHistory"
headers={'Authorization': "Bearer " + TOKEN}

r = requests.get(URL, headers=headers)
j = json.loads(r.text)

print("Uploading file(s) to "+URL)

for root, dirs, files in os.walk(directory):
    for filename in files:
        filepath = os.path.join(root,filename)

        print("Uploading "+filename+"....")
        fileHandle = open(filepath, 'rb')
        
        r = requests.put(URL+"/"+filename+":/content", data=fileHandle, headers=headers)
        fileHandle.close()
        if r.status_code == 200 or r.status_code == 201:
            #remove folder contents
            print("succeeded, removing original file...")
            os.remove(os.path.join(root, filename)) 

print("Script completed")
raise SystemExit
