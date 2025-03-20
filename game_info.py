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

# URL = "https://ncaa-api.henrygd.me/rankings/football/fbs/associated-press"
URL = " https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/scoreboard"
def main():
	# domain = '/scoreboard/football/fbs/2023/13/all-conf'
	domain = ''
	try:
		response = requests.get(URL+domain)
		json_response = json.loads(response.text)
		# response keys = ['leagues', 'groups', 'day', 'events', 'eventsDate'])

		# with open('score_output.json', 'w', encoding='utf-8') as f:
		# 	json.dump(json_response, f, ensure_ascii=False, indent=4)

		events = json_response['events']
		# x=0
		# for item in events:
		# 	print(item['name'])
		# 	if item['name'] == 'Georgia Bulldogs at Gonzaga Bulldogs':
		# 		print(x)
		# 	x+=1

		# in progress game keys = ['id', 'uid', 'date', 'attendance', 'type', 'timeValid', 'neutralSite', 'conferenceCompetition', 'playByPlayAvailable', 'recent', 'venue', 'competitors', 'notes', 'situation', 'status', 'broadcasts', 'tournamentId', 'format', 'startDate', 'broadcast', 'geoBroadcasts', 'highlights']

		competitors = events[3]['competitions'][0]
		print(events[3]['status']['type']['name']) #STATUS_IN_PROGRESS
		# competitors len=2, one for each team

		for team in competitors:
			print()
		with open('score_output.json', 'w', encoding='utf-8') as f:
			json.dump(events[3]['competitions'][0]['competitors'][0], f, ensure_ascii=False, indent=4)


	except Exception as e:
		raise(e)

if __name__=="__main__":
    main()
