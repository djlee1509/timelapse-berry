import datetime
from photo import Photo
from tweet import Tweet
from config import *
from message import Message
import random


def post_tweet(video, msg):
    tweet = Tweet(api_key, secret_key, access_token, access_secret)
    tweet.post(video, msg)


def get_message(today):
    """Returns random maths related message."""
    message = Message(today.month, today.day)
    options = [message.quote_of_today, message.random_math_quote]
    text = f"Did you know? {random.choice(options)}"
    return text


def take_photos(today):
    "Take photo every minute for 12 hours."
    today_date = today.strftime("%Y%m%d")
    photo = Photo(today_date)
    photo.shoot()


def main():
    today = datetime.now()

    tweet_message = get_message(today)
    timelapse_video = take_photos(today)
    post_tweet(timelapse_video, tweet_message)


if __name__ == "__main__":
    main()