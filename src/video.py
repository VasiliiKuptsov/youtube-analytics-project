#from src.channel import youtube
from googleapiclient.discovery import build

import os
#
api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)
print(youtube)


class Video:



    def __init__(self, video_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        try:
            self.__video_id = video_id

            self.video_url = f"https://www.youtube.com/watch?v={video_id}"
            video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
            print(video_response)
            self.video_title = video_response['items'][0]['snippet']['title']
            self.view_count: int = video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = video_response['items'][0]['statistics']['likeCount']
        except IndexError:
            self.__video_id = None

            self.video_url = None

            self.video_title = None
            self.view_count = None
            self.like_count = None


    def __str__(self):
        return f'{self.video_title}'


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):

        super().__init__(video_id)
        self.playlist_id = playlist_id






