import datetime
from photo import Photo
from tweet import Tweet
from config import *
from message import Message
import random
import time


def post_tweet(video, msg):
    tweet = Tweet(api_key, secret_key, access_token, access_secret)
    tweet.post(video, msg)
    print("Completed posting a tweet with timelapse video.")


def get_message(today):
    """Returns random maths related message."""
    message = Message(today.month, today.day)
    options = [message.quote_of_today, message.random_math_quote]
    text = f"Did you know? {random.choice(options)}"
    return text


def take_photos(today_date):
    """Take photo every minute for 12 hours."""
    photo = Photo(today_date)
    photo.shoot()


def main():
    today = datetime.now()
    today_date = today.strftime("%Y%m%d")

    tweet_message = get_message(today)
    take_photos(today_date)
    time.sleep(60)
    
    timelapse_video = open('./videos/{}.mp4'.format(today_date))
    post_tweet(timelapse_video, tweet_message)


if __name__ == "__main__":
    main()