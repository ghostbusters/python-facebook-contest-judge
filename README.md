# python-facebook-contest-judge

Simple script which retrieves a list of likes for a given graph object and chooses a user at random. Helpful for fairly awarding high-volume Facebook contests and giveaways based on liking a post. 

![Facebook Contest Judge](https://media.ghostbusters.net/social/omg-Scoleri-Brothers-ghostbusters2.png "OMG, The Scoleri Brothers!")

## Configure

Be sure to set `fb_access_token` and `fb_post_id` in main.py.

## Install

```
pip install -r requirements.txt
```

## Run

* `python main.py` - extracts all likes for a given post and prints winner, chosen at random, to console.


## Motivation

Needed a quick and fair way to determine the winner of our [Ghostbusters Holiday New Era Cap giveaway](https://www.facebook.com/ghostbusters.net/photos/a.10150213377126164.379141.164743186163/10154539153796164/).

> "That was your whole plan, "get her".  It was scientific." - Dr. Peter Venkman
