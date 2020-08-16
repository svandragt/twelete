import tweepy
import os

from dotenv import load_dotenv
from datetime import datetime, timedelta


def oauth_login(consumer_key, consumer_secret):
    """Authenticate with twitter using OAuth"""
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth_url = auth.get_authorization_url()
    verify_code = input("Authenticate at %s and then enter you verification code here > " % auth_url)
    auth.get_access_token(verify_code)
    return tweepy.API(auth)


load_dotenv(verbose=True)

consumer_key = os.getenv('twelete_consumer_key')
consumer_secret = os.getenv('twelete_consumer_secret')
access_key = os.getenv('twelete_access_key')
access_secret = os.getenv('twelete_access_secret')
days_to_keep = os.getenv('twelete_days_to_keep', default=28)
dry_run = bool(int(os.getenv('twelete_dry_run', 1)))

if dry_run:
    print('Dry run. To delete: add "twelete_dry_run=0" to .env')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
print("Authenticated as: %s" % api.me().screen_name)

timeline = tweepy.Cursor(api.user_timeline).items()

for tweet in timeline:
    tweet_time = datetime.now() - tweet.created_at
    if tweet_time.days > int(days_to_keep):
        print("Deleting %d: [%s] %s" % (tweet.id, tweet.created_at, tweet.text))
        if not dry_run:
            api.destroy_status(tweet.id)
