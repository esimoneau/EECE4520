'''
	Contributors: Emily Simoneau and Cameron Bates
'''
from APICall import APICall
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import json
##from datetime import date, datetime

class TwitterAPI(APICall):	
	def __init__(self):
		APICall.__init__(self)
		with open("twitter_credentials.json", "r") as file:  
			self.creds = json.load(file)
		

	def search(self, keyword, date_start, date_end):
		self.results = {'user': [], 'date': [], 'text': [], 'favorite_count': [], 'user_loc':[], 'retweet_count':[]}
		oauth = OAuth(self.creds['ACCESS_TOKEN'], self.creds['ACCESS_SECRET'], self.creds['CONSUMER_KEY'], self.creds['CONSUMER_SECRET'])
		twitter = Twitter(auth=oauth)
		##date_start_str = self.date_to_string(date_start)
		##date_end_str = self.date_to_string(date_end)
		for status in twitter.search.tweets(q=keyword, until=date_end, since=date_start, result_type='popular', count=100)['statuses']:
			self.results['user'].append(status['user']['screen_name'])
			self.results['date'].append(status['created_at'])
			self.results['text'].append(status['text'])
			self.results['favorite_count'].append(status['favorite_count'])
			self.results['user_loc'].append(status['coordinates'])
			self.results['retweet_count'].append(status['retweet_count'])
	'''
	def date_to_string(self, date_obj) :
		date_string = str(date_obj.year) + '-'
		if date_obj.month < 10:
			date_string += '0'
		date_string += str(date_obj.month) + '-'
		if date_obj.day < 10:
			date_string += '0'
		date_string += str(date_obj.day)
		return date_string
	'''
	def parse_results(self):
		if self.results != {}:
			with open('../json/twitterData.json', 'w') as outfile:
				json.dump(self.results, outfile, indent = 4)
