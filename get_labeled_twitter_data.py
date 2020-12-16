import requests
import json
import pandas as pd
import datetime
import time

df = pd.read_csv('data.csv', names= ['tweet_id', 'user_id', 'label', '1', '2', '3', '4', '5'])

#remove unwanted columns
for i in range(1, 6):
    df.drop([str(i)], axis=1,inplace=True)
    
search_headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAALxKKQEAAAAA%2BpAZV6uMysIeuOhTwt7XEduJeZ4%3DB5i4IC7YL2I8fo5gDZnPOJKLVWy8Ca25bMjcrdPA3LiLhSCiOu'
}
    
search_url = 'https://api.twitter.com/1.1/statuses/show.json?id='

count = 0 

tweets = []
labels = []

for index, row in df.iterrows():
    
    
    search_resp = requests.get(search_url+str(df.loc[index, 'tweet_id']), headers=search_headers)
    
    time.sleep(1)
    
    tweet = search_resp.json()
    
    count += 1
    print(datetime.datetime.now(), count)
    if 'text' not in tweet:
        continue
    else:
        tweets.append(tweet['text'])
        labels.append(1) if df.loc[index, 'label'] == 'y' else labels.append(0)
    

final_df =  pd.DataFrame({'Tweet': tweets, 'Label': labels}, columns=['Tweet', 'Label'])

final_df.to_csv('labelled_tweets.csv', index=False)
