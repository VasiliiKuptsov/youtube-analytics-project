import datetime

from src.video import PlayList

if __name__ == '__main__':
    pl = PlayList('PLekfpYe-gBR88aQVAL76u3FPJ8hpeRkz1')
    #print (pl)

    assert pl.title == "Дима..."
    assert pl.url == "https://www.youtube.com/playlist?list=PLekfpYe-gBR88aQVAL76u3FPJ8hpeRkz1"

    duration = pl.total_duration
    assert str(duration) == "1:49:52"
    assert isinstance(duration, datetime.timedelta)
    assert duration.total_seconds() == 6592.0

    assert pl.show_best_video() == "https://youtu.be/cUGyMzWQcGM"
