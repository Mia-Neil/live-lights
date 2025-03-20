import requests
from bs4 import BeautifulSoup
import sys
import logging
import boto3
import urllib.request
import json
import os
from pprint import pformat
import pprint
import time

logging.getLogger().setLevel(logging.INFO)

URL = 'https://openapi.api.govee.com'
	# (f"get_roster_unique Exception Raised: {e}")

def main():
	my_devices = get_devices()
	for item in my_devices:
		if item['type'] == 'devices.types.light':
			# power_toggle(item['sku'], item['device'], 1)
			color_function(item['sku'], item['device'], 'blue')

def power_toggle(sku, device, command):
	print("power toggle")

def color_function(item['sku'], item['device'], color):
	print('set color')

if __name__=="__main__":
    main()
