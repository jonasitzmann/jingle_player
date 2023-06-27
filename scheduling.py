from apscheduler.schedulers.background import BackgroundScheduler, BaseScheduler
from datetime import timedelta, datetime
from typing import List

from datastructures import Game
from parse_config import Anchor, Jingle
from play_jingle import play_jingle_blocking
from functools import partial
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def run_jobs(scheduler: BaseScheduler):
    scheduler.start()
    yield
    scheduler.shutdown()


def get_default_jingle_list():
    jingle_list = [
        Jingle('Kurz vor Spiel', Anchor.begin, timedelta(minutes=-5), Path('pre_game.mp3')),
        Jingle('Spielbeginn', Anchor.begin, timedelta(0), Path('start.mp3')),
        Jingle('Kurz vor Ende', Anchor.end, timedelta(minutes=-5), Path('pre_end.mp3')),
        Jingle('Spielende', Anchor.end, timedelta(0), Path('end.mp3')),
    ]
    return jingle_list


def schedule_jingles(game_list: List[Game], jingle_list: List[Jingle], play_jingle_func, scheduler: BaseScheduler=None):
    if scheduler is None:
        scheduler = BackgroundScheduler()
    for game in game_list:
        for jingle in jingle_list:
            anchor = game.start if jingle.anchor == Anchor.begin else game.end
            jingle_time = anchor + jingle.offset
            job_name = f'{game.name}_{jingle.name}'
            scheduler.add_job(play_jingle_func, 'date', run_date=jingle_time, name=job_name, args=[jingle.soundfile])
    return scheduler


def main():
    jingle_list = get_default_jingle_list()
    game_list = [
        Game(datetime(2023, 6, 25, 9), datetime(2023, 6, 25, 10, 30), 'Spiel 1'),
        Game(datetime(2023, 6, 25, 9), datetime(2023, 6, 25, 10, 30), 'Finale'),
    ]
    play_jingle_func = partial(play_jingle_blocking, mock=True)
    scheduler = schedule_jingles(game_list, jingle_list, play_jingle_func)
    with run_jobs(scheduler):
        while input('press q to quit') != 'q':
            pass


if __name__ == '__main__':
    main()