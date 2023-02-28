import json
import os

from googleapiclient.discovery import build


class Channel:


    def __init__(self, channel_id):
        self.__channel_id = channel_id

        self.channel = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()

        self.channel_name = self.channel['items'][0]['snippet']['title']
        self.channel_description = self.channel['items'][0]['snippet']['description']
        self.channel_url = self.channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']


    @property
    def channel_id(self):
        return self.__channel_id

    @staticmethod
    def get_service():
        api_key: str = os.getenv('YTapiKey')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube



    def print_info(self):
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))


MondoMedia = Channel('UCxLpKibphYqXrXpxAnR8MfA')
MondoMedia.print_info()
print(MondoMedia.channel_name)
print(MondoMedia.channel_description)
print(MondoMedia.channel_url)
print(MondoMedia.subscriber_count)
print(MondoMedia.video_count)
print(MondoMedia.view_count)

print(MondoMedia.channel_id)
#MondoMedia.channel_id = 'id change'
#print(MondoMedia.channel_id)

print(MondoMedia.get_service())
