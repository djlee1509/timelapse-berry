from twython import Twython


class Tweet:
    def __init__(self, api_key, secret_key, access_token, access_secret):
        self.api_key = api_key
        self.secret_key = secret_key
        self.access_token = access_token
        self.access_secret = access_secret

    def authenticate(self):
        twitter = Twython(self.api_key, self.secret_key, self.access_token, self.access_secret)
        return twitter

    def post(self, video, message):
        with open(video, 'rb') as vid:
            response = self.authenticate().upload_media(media=vid)
            media_id = [response['media_id']]

        self.authenticate().update_status(status=message, media_ids=media_id)
        print(f"Tweeted: {message}")
