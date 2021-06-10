Timelapse-Berry project v1.0 (Work in progress...)

About:
Twitter bot created using Raspberry Pi Zero W and Camera module to take photos every minute for 12 hours then, converted to Timelapse video/ gif which will be uploaded using Python every day.

Problems:-
- Raspberry Pi Zero W doesn't have enough memory to process images and convert to video/ gif.

Next Step:-
- [v] Planning to take photos and upload to Google Cloud Storage.
- Once files uploaded, Google cloud function will be triggered to convert images to video/ gif then, uploaded to twitter.

Created using:-
- Raspberry Pi Zero W, Camera V2, 
- Python: Twython (Twitter API), PiCamera (Raspberry Pi Camera V2)
- API: Numbers API (http://numbersapi.com/), Twitter
