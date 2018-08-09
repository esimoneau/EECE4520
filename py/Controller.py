from NewsAPI import NewsAPI
from redditAPI import RedditAPI
from TwitterAPI import TwitterAPI
import json
from datetime import date, datetime

'''
	Contributors: Chris Lau and Cameron Bates
'''
class SearchParam(object):
	def __init__(self):
		self.startDate = date(2018, 1, 1)
		self.endDate = date(2018, 1, 1)
		self.keyword = ''
		##self.platform = '' - add platform later
		with open('../json/search.json') as jsonFile:
			data = json.load(jsonFile)
			for i in data['searchParams']:
				self.startDate = self.startDate.replace(year=i['startYear'], month=i['startMonth'], day=i['startDay'])
				self.endDate = self.endDate.replace(year=i['endYear'], month=i['endMonth'], day=i['endDay'])
				self.keyword = i['keyword']
				##self.platform = i['platform']
	
def runSearch():
	search_param = SearchParam()
	
	##News API
	news_api = NewsAPI()
	news_start = search_param.startDate.strftime('%Y-%m-%d')
	news_end = search_param.endDate.strftime('%Y-%m-%d')
	news_api.search(search_param.keyword, news_start, news_end)
	news_api.parse_results()
	
	##Social Media API
	##if search_param.platform = 'Twitter' run twitter search
	twitter_api = TwitterAPI()
	twitter_api.search(search_param.keyword, search_param.startDate, search_param.endDate)
	twitter_api.parse_results()
	
	
	##elif search_param.platform = 'Reddit' run reddit search
	reddit_api = RedditAPI()
	reddit_api.search(search_param.keyword, search_param.startDate, search_param.endDate)
	reddit_api.parse_results()
	
