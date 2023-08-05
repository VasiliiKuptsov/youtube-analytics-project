from src.channel import youtube
import datetime
class Video:


    def __init__(self, video_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__video_id = video_id
        self.video_url = f"https://www.youtube.com/watch?v={video_id}"
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        self.video_title = video_response['items'][0]['snippet']['title']
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']


    def __str__(self):
        return f'{self.video_title}'


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):

        super().__init__(video_id)
        self.playlist_id = playlist_id


class PlayList(Video):
    def __init__(self,playlist_id):
        self.__playlist_id = playlist_id
        self.title = 'Дима...'
        self.url = 'https://www.youtube.com/playlist?list=PLekfpYe-gBR88aQVAL76u3FPJ8hpeRkz1'
    @property


    def total_duration(self):
        add_time = datetime.timedelta(minutes = 0)
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        for video in video_response['items']:
            video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=video_id
                                                   ).execute()
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
        print(duration)
        add_time += duration
        return add_time



    def show_best_video(self):

        playlist_id = 'PLekfpYe-gBR88aQVAL76u3FPJ8hpeRkz1'
        playlist_videos = youtube.playlistItems().list(playlistId=playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        # print(playlist_videos)
        like: int = 0
        print(type(like))
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        # print(video_ids)
        for video_id in video_ids:
            print(video_id)
            video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=video_id
                                                   ).execute()
            like_count: int = int(video_response['items'][0]['statistics']['likeCount'])

            if like < like_count:
                url = 'https://youtu.be/' + video_id
                like = like_count

        return url




