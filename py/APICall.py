'''
This class handles all API Calls.
'''

import time
from newsapi import NewsApiClient
import json

class APICall:
	results = {}
	
	def __init__(self, api_key=''):
		self.API_KEY = api_key
	
	def search(self, keyword, date_start, date_end):
		pass
	
	def parse_results():
		pass
	
class NewsAPI(APICall):
	news_sources = 'abc-news,al-jazeera-english,associated-press,bbc-news,cbs-news,cnn,google-news,the-huffington-post,the-new-york-times,the-wall-street-journal,the-washington-post'
	
	def __init__(self, api_key = '1cf0403d680348e29edba0297fb6b5f4'):
		APICall.__init__(self, api_key)
		self.apiClient = NewsApiClient(api_key = self.API_KEY)
		
	def search(self, keyword, date_start='', date_end=''):
		self.results = self.apiClient.get_top_headlines(q=keyword,sources=self.news_sources, language='en')
		if self.results['status'] != 'ok':
			pass
		else:
			if self.results['totalResults'] < 10:
				self.results = self.apiClient.get_everything(q = keyword, sources=self.news_sources, language='en', sort_by='relevancy')
		
	def parse_results(self):
		if self.results != {}:
			with open('../json/newsdata.json', 'w') as outfile:
				json.dump(self.results, outfile)
				
	
class TwitterAPI(APICall):
	pass
	
class RedditAPI(APICall):
	pass