from src.channel import youtube



playlist_id = 'PLekfpYe-gBR88aQVAL76u3FPJ8hpeRkz1'
playlist_videos = youtube.playlistItems().list(playlistId=playlist_id,
                                               part='contentDetails',
                                               maxResults=50,
                                               ).execute()
#print(playlist_videos)
like:int = 0
print(type(like))
video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
#print(video_ids)
for video_id in video_ids:
    print(video_id)
    video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                       id=video_id
                                       ).execute()
    like_count:int = int(video_response['items'][0]['statistics']['likeCount'])

    if like < like_count:
        url =  'https://youtu.be/' + video_id
        like = like_count

print(url)

