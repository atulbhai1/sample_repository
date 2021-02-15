import requests
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:500]:
    url = 'https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json'
    submission_r = requests.get(url)
    response_dict = submission_r.json()
    submission_dict = {'title' : response_dict['title'], 'link' : 'http://news.ycombinator.com/item?id=' + str(submission_id), 'comments' : response_dict.get('descendants', 0)}
    submission_dicts.append(submission_dict)
for submission_dict in submission_dicts:
    print('Title : ', submission_dict['title'])
    print('Discussion Link : ', submission_dict['link'])
    print('Comments : ', submission_dict['comments'])