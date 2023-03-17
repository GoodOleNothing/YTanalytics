from workshop.channel import Channel
from workshop.video import Video
from workshop.plvideo import PLVideo

#
#
#class Channel:
#
#    def __init__(self, channel_id):
#        self.__channel_id = channel_id
#
#        self.channel = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
#
#        self.channel_name = self.channel['items'][0]['snippet']['title']
#        self.channel_description = self.channel['items'][0]['snippet']['description']
#        self.channel_url = self.channel['items'][0]['snippet']['thumbnails']['default']['url']
#        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
#        self.video_count = self.channel['items'][0]['statistics']['videoCount']
#        self.view_count = self.channel['items'][0]['statistics']['viewCount']
#
#    def print_info(self):
#        """Выводит инфо по каналу"""
#        print(json.dumps(self.channel, indent=2, ensure_ascii=False))
#
#    @property
#    def channel_id(self):
#        """Делаем атрибут приватным"""
#        return self.__channel_id
#
#    @staticmethod
#    def get_service():
#        """метод возвращает объект для работы с API ютуба"""
#        api_key: str = os.getenv('YTapiKey')
#        youtube = build('youtube', 'v3', developerKey=api_key)
#        return youtube
#
#    def to_json(self, file_name):
#        """метод, сохраняет информацию по каналу, хранящуюся в атрибутах, в json файл """
#        data = {'Имя канала': self.channel_name, 'Описание канала': self.channel_description,
#                'Ссылка на канал': self.channel_url,
#                'Число подписчиков': self.subscriber_count, 'Количество видео': self.video_count,
#                'Число просмотров': self.view_count}
#        info = open(file_name, 'w', encoding='UTF-8')
#        json.dump(data, info, indent=2, ensure_ascii=False)
#
#    def __str__(self):
#        """выводит название канала"""
#        return f'Youtube-канал: {self.channel_name}'
#
#    def __gt__(self, other) -> bool:
#        """сравнивает кол-во подписчиков"""
#        return int(self.subscriber_count) > int(other.subscriber_count)
#
#    def __add__(self, other):
#        """складывает кол-во подписчиков"""
#        return int(self.subscriber_count) + int(other.subscriber_count)
#
#
#class Video:
#
#    def __init__(self, video_id):
#        self.video_id = video_id
#
#        self.video = self.get_api_object().videos().list(id=self.video_id, part='snippet,statistics').execute()
#
#        self.video_name = self.video['items'][0]['snippet']['title']
#        self.view_count = self.video['items'][0]['statistics']['viewCount']
#        self.like_count = self.video['items'][0]['statistics']['likeCount']
#
#    @staticmethod
#    def get_api_object():
#        """метод возвращает объект для работы с API ютуба"""
#        api_key: str = os.getenv('YTapiKey')
#        youtube = build('youtube', 'v3', developerKey=api_key)
#        return youtube
#
#    def __str__(self):
#        """выводит название видео"""
#        return self.video_name
#
#
#class PLVideo(Video):
#
#    def __init__(self, video_id, pl_id):
#        self.pl_id = pl_id
#        super().__init__(video_id)
#
#        self.pl = self.get_api_object().playlists().list(id=self.pl_id, part='snippet').execute()
#
#        self.pl_name = self.pl['items'][0]['snippet']['title']
#
#    def __str__(self):
#        """выводит название видео и название плейлиста"""
#        return f'{self.video_name} ({self.pl_name})'

#MondoMedia = Channel('UCxLpKibphYqXrXpxAnR8MfA')
#MondoMedia.print_info()

#print(MondoMedia.channel_name)
#print(MondoMedia.channel_description)
#print(MondoMedia.channel_url)
#print(MondoMedia.subscriber_count)
#print(MondoMedia.video_count)
#print(MondoMedia.view_count)
#
#print(MondoMedia.channel_id)
##MondoMedia.channel_id = 'id change'
#
#
#print(MondoMedia.get_service())
#
#MondoMedia.to_json('Mondo.json')

#print(MondoMedia)
#vDud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
#print(vDud)
#print(MondoMedia > vDud)
#print(MondoMedia < vDud)
#print(MondoMedia + vDud)


video1 = Video('9lO06Zxhu88')
print(video1)
video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
print(video2)
