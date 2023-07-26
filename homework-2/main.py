from src.channel import Channel

if __name__ == '__main__':

    vasyanasene = Channel('UCUQCJV9ksyRXe0sCH5noWNg')

    # получаем значения атрибутов
    print(vasyanasene.title)  # ВАСЯ НА СЕНЕ
    print(vasyanasene.video_count)  # 211 (может уже больше)
    print(vasyanasene.url)  # https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A
    print(vasyanasene.print_info())
    # менять не можем
    vasyanasene.channel_id = 'Новое название'
    # AttributeError: property 'channel_id' of 'Channel' object has no setter

    # можем получить объект для работы с API вне класса
    print(Channel.get_service())
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

    # создаем файл 'moscowpython.json' в данными по каналу
    vasyanasene.to_json('moscowpython.json')
