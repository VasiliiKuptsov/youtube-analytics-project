import datetime
from src.playlist import PlayList
#from src.video import PlayList

if __name__ == '__main__':
    pl = PlayList('PLekfpYe-gBR88aQVAL76u3FPJ8hpeRkz1')

    assert pl.title == "Дима..."
    assert pl.url == "https://www.youtube.com/playlist?list=PLekfpYe-gBR88aQVAL76u3FPJ8hpeRkz1"

    duration = pl.total_duration
    assert str(duration) == "6:28:55"
    assert isinstance(duration, datetime.timedelta)
    assert duration.total_seconds() == 23335.0
    assert pl.show_best_video() == "https://youtu.be/vwzIXP9k6_8"