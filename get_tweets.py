import tweepy
from tweepy import OAuthHandler
import json

# consumer key, consumer secret, access token, access secret.
# replace with your own
ckey = "..."
csecret = "..."
atoken = "..."
asecret = "..."


class MyStreamListener(tweepy.StreamListener):
    f = None

    def __init__(self, api=None):
        self.f = open("tweets.txt", "w+")

    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        self.f.write('\"{}\"\n'.format(tweet))
        print(tweet)
        return(True)

    def on_status(self, status):
        print(status.text)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

myStream = tweepy.Stream(auth=auth, listener=MyStreamListener())
myStream.filter(track=['#BringBackNationalDex'])
