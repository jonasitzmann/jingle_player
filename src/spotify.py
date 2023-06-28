import logging
from contextlib import contextmanager
from typing import Optional

from pytify.cli import get_pytify_class_by_platform
from pytify.pytifylib import Pytifylib


class PytifyMock:
    def pause(self):
        logging.info("pause spotify")

    def play_pause(self):
        logging.info("play_pause spotify")


def get_pytify(mock=False):
    return PytifyMock() if mock else get_pytify_class_by_platform()()


@contextmanager
def except_all():
    try:
        yield
    except Exception:
        ...


@contextmanager
def pause_spotify(mock_pytify: False = None, mock=False):
    if mock_pytify:
        pytify = PytifyMock()
    else:
        with except_all():
            pytify = get_pytify_class_by_platform()()
    with except_all():
        pytify.pause()
    yield
    with except_all():
        pytify.play_pause()
