from picamera import PiCamera
import time
import os
from picamera import PiCamera
from google.cloud import storage


class Photo:
    def __init__(self, today):
        self.today = today
        self.image_dir = "./images/{}".format(self.today)
        self.fps = 30

    def shoot(self):
        """Check if the image directory exists. if not, it will create a directory to save."""
        if not os.path.isdir(self.image_dir):
            os.mkdir(self.image_dir)
        self.run()

    def run(self):
        """Take photos every minute and save in the image directory."""
        camera = PiCamera()
        i = 0

        while i < 720:
            img = os.path.join(self.image_dir, "image_{0:04d}.jpg".format(i))
            camera.capture(img)
            i += 1
            time.sleep(60)

        print("Finished Taking Photos. Now converting images to video.")
        time.sleep(60)

    def upload_to_bucket(self, json_path, bucket_name):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_path
        client = storage.Client()
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(self.today)

        for file_name in os.listdir(self.image_dir):
            blob = bucket.blob("{}/{}".format(self.today, file_name))
            source_file_name = os.path.join(self.image_dir, file_name)
            blob.upload_from_filename(source_file_name)

            print("File Uploaded Successfully: {}".format(file_name))