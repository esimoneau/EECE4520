'''
This class handles all NewsAPI calls.
'''

from APICall import APICall
from newsapi import NewsApiClient
import json

class NewsAPI(APICall):
	news_sources = 'abc-news,al-jazeera-english,associated-press,bbc-news,cbs-news,cnn,google-news,the-huffington-post,the-new-york-times,the-wall-street-journal,the-washington-post'
	
	def __init__(self, API_KEY = '1cf0403d680348e29edba0297fb6b5f4'):
		self.apiClient = NewsApiClient(api_key = API_KEY)
		
	def search(self, keyword, date_start, date_end):
		self.results = self.apiClient.get_everything(q=keyword,sources = self.news_sources,from_param=date_start,to=date_end,language='en',sort_by='popularity', page_size=20)
		
	def parse_results(self):
		with open('../json/newsData.json', 'w') as outfile:
			json.dump(self.results, outfile)
				