import sys
import time
import math
import pandas as pd
from twython import Twython
from datetime import datetime

consumer_key = 'YOUR CONSUMER KEY HERE'
consumer_secret = 'YOUR CONSUMER SECRET HERE'
token = 'YOUR TOKEN HERE'
token_secret = 'YOUR TOKEN SECRET HERE'

twitter = Twython(consumer_key, consumer_secret, token, token_secret)

def main():
        kia = pd.read_csv(sys.argv[1], sep='|')
        now = datetime.now()
        year = now.year
        day = now.day
        month = now.month
        buffer_seconds = 120
        remaining_secs = (datetime(year, month, day+1) - datetime.now()).total_seconds() - buffer_seconds

        tweets = kia[(kia['dayDeath'] == day) & (kia['monthDeath'] == month)]['tweet'].values
        delay = math.floor(remaining_secs / len(tweets))

        for tweet in tweets:
                twitter.update_status(status=tweet)
                time.sleep(delay)

if __name__ == '__main__':
        main()
