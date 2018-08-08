from datetime import date, datetime
import praw
import json

reddit = praw.Reddit(user_agent = 'userAgent', client_id = 'Wtyt6ZzLdbI6NA', client_secret = '3BxHtc7XdjL28i-xRS_NQPMV_P4')

subData = {}
subData['submissions'] = []
subData['todaySubs'] = []

class SearchParam(object):
    def __init__(self):
        self.startDate = date(2018, 1, 1)
        self.endDate = date(2018, 1, 1)
        self.keyword = ''

def addParams(search):
    with open('search.json') as jsonFile:
        data = json.load(jsonFile)
        for i in data['searchParams']:
            search.startDate = search.startDate.replace(year=i['startYear'], month=i['startMonth'], day=i['startDay'])
            search.endDate = search.endDate.replace(year=i['endYear'], month=i['endMonth'], day=i['endDay'])
            search.keyword = i['keyword']

def get_date(submission):
    time = submission.created
    return date.fromtimestamp(time)

def get_datetime(submission):
    time = submission.created
    return datetime.fromtimestamp(time)

def getSubmissions(keyword, dateStart, dateEnd):
    for submission in reddit.subreddit('politics+worldnews').top(limit = None):
        if keyword.lower() in str(submission.title).lower() and (get_date(submission) > dateStart and get_date(submission) < dateEnd):
            subData['submissions'].append({
                'title': str(submission.title),
                'subreddit': str(submission.subreddit),
                'score': int(submission.score),
                'comments': int(submission.num_comments),
                'date created': str(get_datetime(submission).date()),
                'time created': str(get_datetime(submission).time())
            })                   

search = SearchParam()
addParams(search)

getSubmissions(search.keyword, search.startDate, search.endDate)

with open('redditData.json', 'w') as outfile:
    json.dump(subData, outfile)
