from pytify.cli import get_pytify_class_by_platform
from typing import Optional
from pytify.pytifylib import Pytifylib
from contextlib import contextmanager
import logging


class PytifyMock:
    def pause(self):
        logging.info('pause spotify')

    def play_pause(self):
        logging.info('play_pause spotify')


def get_pytify(mock=False):
    return PytifyMock() if mock else get_pytify_class_by_platform()()


@contextmanager
def pause_spotify(pytify: Optional[Pytifylib] = None, mock=False):
    if pytify is None:
        pytify = PytifyMock() if mock else get_pytify_class_by_platform()()
    try:
        pytify.pause()
    except Exception as ex:
        logging.warning(f'could not pause Spotify: \n {ex}')
    yield
    try:
        pytify.play_pause()
    except Exception as ex:
        logging.warning(f'could not play_pause Spotify: \n {ex}')


