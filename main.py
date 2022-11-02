import requests
import json

send_url = "http://api.ipstack.com/check?access_key=d71baf765e56c2bf54a6e5e30511db30"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
latitude = geo_json['latitude']
longitude = geo_json['longitude']
city = geo_json['city']
print(geo_json)
