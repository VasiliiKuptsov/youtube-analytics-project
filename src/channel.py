import json
from googleapiclient.discovery import build
import os

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)
class Channel:

    #API_KEY = os.getenv('YT_API_KEY')
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        channel = youtube.channels().list(id=self.__channel_id, part='snippet, statistics').execute()
        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = f"https://www.youtube.com/{channel['items'][0]['snippet']['customUrl']}"
        self.subscriber_count = channel['items'][0]['statistics']['subscriberCount']
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.view_count = channel['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(f'Channel ID: {self.channel_id}\n'
            f'Title: {self.title}\n'
            f'Descripstion: {self.description}\n'
            f'Channel url: {self.url}\n'
            f'Subscriber count: {self.subscriber_count}\n'
            f'Video count: {self.video_count}\n'
            f'View count: {self.view_count}')


    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        return youtube

    def to_json(self, filename):
        with open (filename, 'w') as file:
            data = {'ID': self.channel_id,
            'Title': self.title,
            'Descripstion': self.description,
            'Channel url': self.url,
            'Subscriber count': self.subscriber_count,
            'Video count': self.video_count,
            'View count': self.view_count}
            json.dump(data, file, ensure_ascii=False)