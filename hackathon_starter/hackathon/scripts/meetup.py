'''
meetup.py aggregates various data from meetup.com.
'''

import requests
import simplejson as json

USERDATA = 'https://api.meetup.com/2/member/self/?access_token='

def retrieveUserData(url):
	req = requests.get(url)
	content = json.loads(req.content)
	filteredData = []
	data = {}
	data['name'] = content['name']
	data['country'] = content['country'].upper()
	data['city'] = content['city']
	data['state'] = content['state']
	data['status'] = content['status']
	filteredData.append(data)
	return filteredData

def retrieveDashboard(url):
	req = requests.get(url)
	return req.content
	

