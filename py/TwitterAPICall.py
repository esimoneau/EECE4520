import json

# Search tweets
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': [], 'user_loc':[]}  
for status in python_tweets.search(**query)['statuses']:  
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])
    dict_['user_loc'].append(status['user']['location'])

# Structure data in a pandas DataFrame for easier manipulation
with open("search_results.json", "w") as file:
    json.dump(dict_, file)
