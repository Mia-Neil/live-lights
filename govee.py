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
			get_state(item, key)
			# light_on_off(item, key, 1)
			# get_dynamic_scene(item, key)
			# set_dynamic_scene(item, key, True)
			# rgb_value = govee_color(232,119,34)
			# set_rgb_color(item, key, 16337920)
			# set_segment_color(item, key, govee_color(0, 12, 102), govee_color(150, 81, 0))


def govee_color(red, green, blue):
	return((((red * 256 ) + green) * 256) + blue)

def set_dynamic_scene(device, key, diy=False):
	# Scene Name: Maize & Blue Flash
	# Value: 15454926

	url = '/router/api/v1/device/control'

	payload = {
		"requestId": "uuid",
		"payload": {
			"sku": device['sku'],
			"device": device['device'],
			"capability": {
				"type": "devices.capabilities.dynamic_scene",
				"instance": "lightScene",
				"value": {
					"id": 9096,
					"paramId": 15183
				}
			}
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

def get_dynamic_scene(device, key, diy=False):
	payload = {
		"requestId": "uuid",
		"payload": {
			"sku": device['sku'],
			"device": device['device']
		}
	}
	headers = {'Govee-API-Key': key, 'Content-Type': 'application/json'}

	if diy:
		url = '/router/api/v1/device/diy-scenes'
	else:
		url = '/router/api/v1/device/scenes'

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

def light_on_off(device, key, power):

		url = '/router/api/v1/device/control'
		payload = {
			"requestId": "uuid",
			"payload": {
				"sku": device['sku'],
				"device": device['device'],
				"capability": {
					"type": "devices.capabilities.on_off",
					"instance": "powerSwitch",
					"value": power
				}
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

def set_segment_color(device, key, color1, color2):
	url = '/router/api/v1/device/control'
	payload = {
		"requestId": "uuid",
		"payload": {
			"sku": device['sku'],
			"device": device['device'],
			"capability": {
				"type": "devices.capabilities.segment_color_setting",
				"instance": "segmentedColorRgb",
				"value": {
						"segment":[0,2,4,6,8,10,12,14],
						"rgb": color1
					  }
			}
		}
	}
	payload2 = {
		"requestId": "uuid",
		"payload": {
			"sku": device['sku'],
			"device": device['device'],
			"capability": {
				"type": "devices.capabilities.segment_color_setting",
				"instance": "segmentedColorRgb",
				"value": {
						"segment":[1, 3, 5, 7, 9, 11, 13],
						"rgb": color2
					  }
			}
		}
	}
	headers = {'Govee-API-Key': key, 'Content-Type': 'application/json'}
	try:
		response = requests.post(URL+url, json=payload, headers=headers)
		response = requests.post(URL+url, json=payload2, headers=headers)
		json_response = json.loads(response.text)
		with open('govee_output.json', 'w', encoding='utf-8') as f:
			json.dump(json_response, f, ensure_ascii=False, indent=4)
		return(json_response)
	except Exception as e:
		raise(e)

def set_rgb_color(device, key, rgb_value):
	url = '/router/api/v1/device/control'
	payload = {
		"requestId": "uuid",
		"payload": {
			"sku": device['sku'],
			"device": device['device'],
			"capability": {
				"type": "devices.capabilities.color_setting",
				"instance": "colorRgb",
				"value": rgb_value
			}
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


if __name__=="__main__":
	main()
