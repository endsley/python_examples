#!/usr/bin/env python


import requests
from pprint import pprint

def check_valid_youtube_link(videoID, api_key):
	url = f'https://www.googleapis.com/youtube/v3/videos?id=%s&key=%s&part=status'%(videoID, api_key)
	url_get = requests.get(url)
	response = url_get.json()
	if len(response['items']) == 0:
		return False
	else:
		try:
			return response['items'][0]['status']['publicStatsViewable']
		except:
			return False



if __name__ == "__main__": 
	api_key = 'yourKey'			# Go to google app engine to enable and get this key
	#videoID = '9XgbxU7FFbU'
	videoID = '9Xgbx'
	
	
	valid = check_valid_youtube_link(videoID, api_key)
	print('Link %s is valid : %r'%(videoID, valid))

