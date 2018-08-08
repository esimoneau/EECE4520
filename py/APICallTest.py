'''
Test Framework for API Calls.
'''

import APICall
import time
from newsapi import NewsApiClient

def main():
	news_api = APICall.NewsAPI()
	news_api.search('bitcoin')
	news_api.parse_results()
	input("press enter to continue ")
	
if __name__ == '__main__':
	main()
