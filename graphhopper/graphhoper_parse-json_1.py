import requests 
import urllib.parse 

geocode_url = "https://graphhopper.com/api/1/geocode?" 
route_url = "https://graphhopper.com/api/1/route?" 
loc1 = "Belgium, Vilvoorde" 
loc2 = "Belgium, Elsene" 
key = "090326cd-b755-4214-b7f8-b10bc7010b04"      
# Replace with your Graphhopper API key 

url = geocode_url + urllib.parse.urlencode({"q":loc1, "limit": "1", "key":key})

replydata = requests.get(url) 
json_data = replydata.json() 
json_status = replydata.status_code 
print(json_data) 