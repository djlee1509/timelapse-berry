from picamera import PiCamera
import time
import os
from datetime import datetime


class Photo:
    def __init__(self, today):
        self.image_dir = f"./{today}_images"

    def run(self):
        """Check if the image directory exists. if not, it will create a directory to save."""
        if not os.path.isdir(self.image_dir):
            os.mkdir(self.image_dir)
        self.capture()

    def capture(self):
        """Take photos every minute and save in the image directory."""
        camera = PiCamera()
        i = 0

        while i < 720:
            img = os.path.join(self.image_dir, "image_{0:04d}.jpg".format(i))
            camera.capture(img)
            i += 1
            time.sleep(60)
