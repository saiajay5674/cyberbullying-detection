import requests


search_headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAALxKKQEAAAAA%2BpAZV6uMysIeuOhTwt7XEduJeZ4%3DB5i4IC7YL2I8fo5gDZnPOJKLVWy8Ca25bMjcrdPA3LiLhSCiOu'
}

search_url = 'https://api.twitter.com/1.1/statuses/show.json?id=210462857140252672'

search_resp = requests.get(search_url, headers=search_headers)

print(search_resp.json())