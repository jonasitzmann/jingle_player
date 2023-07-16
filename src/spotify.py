import logging
from contextlib import contextmanager
from typing import Optional

from pytify.cli import get_pytify_class_by_platform
from pytify.pytifylib import Pytifylib
import pytify
from src.pytify_dbus_interface_override import Interface as InterfaceOverride
from pytify.dbus import interface

interface.Interface = InterfaceOverride


class PytifyMock:
    def pause(self):
        logging.debug("pause spotify")

    def play_pause(self):
        logging.debug("play_pause spotify")


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
