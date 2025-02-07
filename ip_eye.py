import requests
import json

ip_request = requests.get('https://get.geojs.io/v1/ip.json')
ip = str(input("Enter target ip : ")) #ip_request.json() => {ip:'XXX.XXX.XX.X'}
print(ip) #ex:198.975.33.4
geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + ip + '.json' 
geo_request = requests.get(geo_request_url)
geo_data = geo_request.json()
for key in geo_data.keys():
	print(key, ":{}".format(geo_data[key]))
