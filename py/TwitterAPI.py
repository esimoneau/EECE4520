'''
	Contributors: Emily Simoneau and Cameron Bates
'''
from APICall import APICall
from twython import Twython
import json

class TwitterAPI(APICall):	
	def __init__(self):
		APICall.__init__(self)
		with open("twitter_credentials.json", "r") as file:  
			self.creds = json.load(file)
		

	def search(self, keyword, date_start='', date_end=''):
		self.results = {'user': [], 'date': [], 'text': [], 'favorite_count': [], 'user_loc':[]}
		python_tweets = Twython(self.creds['CONSUMER_KEY'], self.creds['CONSUMER_SECRET'])
		for status in python_tweets.search(q=keyword)['statuses']:
			self.results['user'].append(status['user']['screen_name'])
			self.results['date'].append(status['created_at'])
			self.results['text'].append(status['text'])
			self.results['favorite_count'].append(status['favorite_count'])
			self.results['user_loc'].append(status['user']['location'])

	def parse_results(self):
		if self.results != {}:
			with open('../json/twitterData.json', 'w') as outfile:
				json.dump(self.results, outfile)