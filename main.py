import facebook
import requests
import random


fb_access_token = '' # Replace with valid Access Token
fb_post_id = '10154539153796164' # Replace with valid Facebook Graph ID object for your contest 

graph = facebook.GraphAPI(access_token=fb_access_token)
entries = []

while True:
  if not entries:
    likes = graph.get_connections(id=fb_post_id, connection_name='likes')
  else:
    likes = requests.get(likes['paging']['next']).json()
  for like in likes['data']:
    entries.append(like)
  if not likes.get('paging').get('next'):
    break

random.seed()
winner_index = random.randint(0,len(entries) - 1)

print 'Out of ' + str(len(entries)) + ' entries...'
print 'The winner is ' + str(entries[winner_index])
print 'That wasn\'t such a chore now, was it?'
