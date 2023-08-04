from src.video import Video, PLVideo

if __name__ == '__main__':
    # Создаем два экземпляра класса
    video1 = Video('AWX4JnAnjBE')  # 'AWX4JnAnjBE' - это id вид

    video2 = PLVideo('sSBQHHm5VhY', 'PLekfpYe-gBR-Xq2_7E_EUl6mVysXOEJ4q')
    assert str(video1) == 'GIL в Python: зачем он нужен и как с этим жить'
    assert str(video2) == 'ДЕВУШКА ИЗ ЗАБРОШЕННОЙ ДЕРЕВНИ СТАЛА ХОДИТЬ.10 лет её не правильно лечили.'

