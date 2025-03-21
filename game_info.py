import requests
import urllib.request
import json
from pprint import pformat
import pprint

# Option + CMD + left or right arrow

# https://stats.ncaa.org/
# https://github.com/henrygd/ncaa-api

# https://gist.github.com/akeaswaran/b48b02f1c94f873c6655e7129910fc3b?permalink_comment_id=4995211

# https://sportsdata.io/developers/api-documentation/ncaa-basketball#games--by-date-live--final
# Free tier, but requires signing up

# https://www.thesportsdb.com/

URL = 'https://ncaa-api.henrygd.me'

def main():
	# espn_hidden()
	ncaa_api()



def ncaa_api():
	url = '/scoreboard/basketball-men/d1/2025'

	# print(URL+url)
	try:
		response = requests.get(URL+url)
		json_response = json.loads(response.text)
	except Exception as e:
		raise(e)

	games = json_response['games']
	for game in games:
		away = game['game']['away']
		print(f"\nGameID:{game['game']['gameID']}")
		print(f"{away['names']['short']}: {away['score']}")
		home = game['game']['home']
		print(f"{home['names']['short']}: {home['score']}")

	# with open('score_output.json', 'w', encoding='utf-8') as f:
	# 	json.dump(json_response['games'], f, ensure_ascii=False, indent=4)

def ncaa_get_schools():
	endpoint = '/schools-index'
	try:
		response = requests.get(URL+endpoint)
		json_response = json.loads(response.text)
	except Exception as e:
		raise(e)
	return(json_response)

def espn_hidden():
	url = "https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/scoreboard"

	try:
		response = requests.get(url)
		json_response = json.loads(response.text)

	except Exception as e:
		raise(e)

	events = json_response['events']
	for item in events:
		print(f"Event Name: {item['name']}")
		print(f"Game Status: {item['status']['type']['name']}")

		competitors = item['competitions'][0]
		for team in competitors['competitors']:
			team_name = team['team']['displayName']
			score = team['score']
			print(f"{team_name}: {score}")
		print("\n**************************************************\n")

		# with open('score_output.json', 'w', encoding='utf-8') as f:
		# 	json.dump(events[2]['competitions'][0]['competitors'][0], f, ensure_ascii=False, indent=4)

if __name__=="__main__":
    main()
