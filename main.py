from datastructures import Game
import logging
from play_jingle import play_jingle_blocking
import calendar_handling
import spotify
from functools import partial
from typing import List, Optional
from scheduler import Scheduler
from argparse import ArgumentParser
from runpy import run_path
from parse_config import Config, Anchor, Jingle


def schedule_jingles(game_list: List[Game], jingle_list: List[Jingle], play_jingle_func, scheduler: Optional[Scheduler]=None):
    if scheduler is None:
        scheduler = Scheduler()
    for game_id, game in enumerate(game_list):
        for jingle_id, jingle in enumerate(jingle_list):
            anchor = game.start if jingle.anchor == Anchor.begin else game.end
            job_date = anchor + jingle.offset
            job_name = f'{game.name}: {jingle.name}'
            job_id = f'{game_id}_{jingle_id}'
            job_fn = partial(play_jingle_func, jingle.soundfile)
            scheduler.add_job(job_fn, job_date, job_id, name=job_name)
    return scheduler


def run(cfg: Config):
    mock = cfg.mocking
    logging.basicConfig(format='%(asctime)s %(levelname)-6s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
    games = calendar_handling.get_games_from_cfg(cfg.calendar)
    pytify = spotify.get_pytify(mock=mock.mock_spotify)
    play_jingle_func = partial(play_jingle_blocking, pytify=pytify, mock=mock.mock_jingle_playback)
    scheduler = schedule_jingles(games, cfg.jingles.jingles, play_jingle_func)
    scheduler.main_loop(simulate_waiting=mock.simulate_waiting, begin_before_1st_job=mock.begin_before_1st_job)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--config', default='config.py')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    cfg: Config = run_path(args.config)['config']
    run(cfg)


if __name__ == '__main__':
    main()
