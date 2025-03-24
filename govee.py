import requests
import urllib.request
import json
from pprint import pformat
import pprint


URL = 'https://openapi.api.govee.com'

def main():
	f = open("api_key", "r")
	key = f.read().replace('\n', '')

	my_devices = get_devices(key)

	for item in my_devices:
		if item['type'] == 'devices.types.light':
			print(item['deviceName'])
			# get_state(item, key)
			get_dynamic_scene(item, key)

def get_dynamic_scene(device, key):
	url = '/router/api/v1/device/scenes'
	payload = {
		"requestId": "uuid",
		"payload": {
			"sku": device['sku'],
			"device": device['device']
		}
	}
	headers = {'Govee-API-Key': key, 'Content-Type': 'application/json'}
	try:
		response = requests.post(URL+url, json=payload, headers=headers)
		json_response = json.loads(response.text)
		with open('govee_output.json', 'w', encoding='utf-8') as f:
			json.dump(json_response, f, ensure_ascii=False, indent=4)
		return(json_response)
	except Exception as e:
		raise(e)

def get_state(device, key):
	url = '/router/api/v1/device/state'
	payload = {
		"requestId": "uuid",
		"payload": {
			"sku": device['sku'],
			"device": device['device']
		}
	}
	headers = {'Govee-API-Key': key, 'Content-Type': 'application/json'}
	try:
		response = requests.post(URL+url, json=payload, headers=headers)
		json_response = json.loads(response.text)
		with open('govee_output.json', 'w', encoding='utf-8') as f:
			json.dump(json_response, f, ensure_ascii=False, indent=4)
		return(json_response)
	except Exception as e:
		raise(e)


def get_devices(key):
	url = '/router/api/v1/user/devices'
	headers = {'Govee-API-Key': key, 'Content-Type': 'application/json'}

	try:
		response = requests.get(URL+url, headers=headers)
		json_response = json.loads(response.text)
		return(json_response['data'])
		# for product in json_response['data']:
		# 	print(product['deviceName'])

		# with open('govee_output.json', 'w', encoding='utf-8') as f:
		# 	json.dump(json_response, f, ensure_ascii=False, indent=4)

	except Exception as e:
		raise(e)


if __name__=="__main__":
	main()
