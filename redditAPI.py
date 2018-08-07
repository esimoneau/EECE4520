from datetime import date
import praw
import json

reddit = praw.Reddit(user_agent = 'userAgent', client_id = 'Wtyt6ZzLdbI6NA', client_secret = '3BxHtc7XdjL28i-xRS_NQPMV_P4')

subs = []
subData = {}
subData['submissions'] = []

startDate = date(2018, 1, 1)
endDate = date(2018, 8, 6)

def get_date(submission):
    time = submission.created
    return date.fromtimestamp(time)

def getSubmissions(keyword, dateStart, dateEnd, listOfSubs):
    total = 0
    for submission in reddit.subreddit('politics+worldnews').top(limit = None):
        if keyword.lower() in str(submission.title).lower() and (get_date(submission) > dateStart and get_date(submission) < dateEnd):
            total += 1
            listOfSubs.append(submission)
            subData['submissions'].append({
                'title': str(submission.title),
                'subreddit': str(submission.subreddit),
                'score': int(submission.score),
                'comments': int(submission.num_comments),
                'date created': str(get_date(submission))
            })            
    print(total)
    return listOfSubs
    
getSubmissions('Trump', startDate, endDate, subs)

with open('subData.txt', 'w') as outfile:
    json.dump(subData, outfile)