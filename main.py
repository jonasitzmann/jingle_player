import logging
from argparse import ArgumentParser
from functools import partial
from runpy import run_path
from typing import List, Optional

from src import calendar_handling
from src.config import Config, Anchor, Jingle
from src.datastructures import Game
from src.play_jingle import play_jingle_blocking
from src.scheduler import Scheduler


def schedule_jingles(
    game_list: List[Game],
    jingle_list: List[Jingle],
    play_jingle_func,
    scheduler: Optional[Scheduler] = None,
):
    if scheduler is None:
        scheduler = Scheduler()
    for game_id, game in enumerate(game_list):
        for jingle_id, jingle in enumerate(jingle_list):
            anchor = game.start if jingle.anchor == Anchor.begin else game.end
            job_date = anchor + jingle.offset
            job_name = f"{game.name}: {jingle.name}"
            job_id = f"{game_id}_{jingle_id}"
            job_fn = partial(play_jingle_func, jingle.soundfile)
            scheduler.add_job(job_fn, job_date, job_id, name=job_name)
    return scheduler


def run(cfg: Config):
    mock = cfg.mocking
    logging.basicConfig(
        format="%(asctime)s %(message)s",
        level=logging.INFO,
        # datefmt="%Y-%m-%d %H:%M:%S",
        datefmt="%a %H:%M:%S",
    )
    games = calendar_handling.get_games_from_cfg(cfg.calendar)
    play_jingle_func = partial(
        play_jingle_blocking,
        mock_pytify=mock.mock_spotify,
        mock=mock.mock_jingle_playback,
    )
    scheduler = schedule_jingles(games, cfg.jingles.jingles, play_jingle_func)
    try:
        scheduler.main_loop(
            simulate_waiting=mock.simulate_waiting,
            begin_before_1st_job=mock.begin_before_1st_job,
        )
    except KeyboardInterrupt:
        ...


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--config", default="configs/config.py")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    cfg: Config = run_path(args.config)["config"]
    run(cfg)


if __name__ == "__main__":
    main()
