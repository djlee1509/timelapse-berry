from picamera import PiCamera
import time
import os


class Photo:
    def __init__(self, today):
        self.today = today
        self.image_dir = f"./images/{self.today}"
        self.fps = 30

    def shoot(self):
        """Check if the image directory exists. if not, it will create a directory to save."""
        if not os.path.isdir(self.image_dir):
            os.mkdir(self.image_dir)
        self.run()

    def convert_images_to_video(self):
        """Convert images to Video"""
        os.system('ffmpeg -r {} -f image2 -s 1024x768 -nostats -loglevel 0 -pattern_type glob -i "{}/*.jpg" -vcodec libx264 -crf 25  -pix_fmt yuv420p ./videos/{}.mp4'.format(self.fps, self.image_dir, self.today))
        print('Timelapse video is complete. Video saved as ./videos/{}.mp4'.format(self.today))


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

        self.convert_images_to_video()

    # def create_storage_bucket(self):
    #     storage_client = storage.Client()
    #     bucket_name = f"{self.today}_images"
    #     bucket = storage_client.create_bucket(bucket_name)
    #     print("Bucket {} created.".format(bucket.name))

    #     for img in os.listdir(self.image_dir):
    #         src_file = os.path.join(self.image_dir, img)
    #         self.upload_blob(bucket_name, src_file, img)

    # def upload_blob(self, bucket_name, source_file_name, destination_blob_name):
    #     """Uploads a file to the bucket."""
    #     # The ID of your GCS bucket
    #     # bucket_name = "your-bucket-name"
    #     # The path to your file to upload
    #     # source_file_name = "local/path/to/file"
    #     # The ID of your GCS object
    #     # destination_blob_name = "storage-object-name"

    #     storage_client = storage.Client()
    #     bucket = storage_client.bucket(bucket_name)
    #     blob = bucket.blob(destination_blob_name)

    #     blob.upload_from_filename(source_file_name)

    #     print(
    #         "File {} uploaded to {}.".format(
    #             source_file_name, destination_blob_name
    #         )
    #     )