from datetime import timedelta
from dataclasses import dataclass, KW_ONLY
from enum import Enum
from pathlib import Path
from typing import List, Optional
from runpy import run_path
from pytimeparse.timeparse import timeparse
import logging


class Anchor(Enum):
    begin = 'begin'
    end = 'end'


@dataclass
class Jingle:
    name: str
    _ = KW_ONLY
    soundfile: Path | str = None
    anchor: Anchor | str = Anchor.begin
    offset: timedelta | str = timedelta(0)

    def __post_init__(self):
        if self.soundfile is None:
            self.soundfile = Path(self.name + '.mp3')
        if isinstance(self.offset, str):
            self.offset = timedelta(seconds=timeparse(self.offset))
        if isinstance(self.anchor, str):
            self.anchor = Anchor[self.anchor.lower()]


@dataclass
class JingleConfig:
    _ = KW_ONLY
    jingles: List[Jingle] = None
    jingle_dir: Path = Path('jingles')

    def __post_init__(self):
        if not self.jingles:
            logging.warning('no jingles configured!')
            self.jingles = []
        for jingle in self.jingles:
            jingle.soundfile = self.jingle_dir / jingle.soundfile
            if not jingle.soundfile.is_file():
                logging.warning(f'sound file does not exist: {jingle.soundfile}')


@dataclass
class CalendarConfig:
    _ = KW_ONLY
    calendar_url: str
    calendar_file: str
    download_calendar: bool = True


@dataclass
class MockingConfig:
    _ = KW_ONLY
    mock_spotify: bool = False
    mock_jingle_playback: bool = False
    simulate_waiting: bool = False
    begin_before_1st_job: Optional[timedelta] = False

    @staticmethod
    def mock_everything():
        return MockingConfig(
            mock_spotify=True,
            mock_jingle_playback=True,
            simulate_waiting=True,
            begin_before_1st_job=None,
        )

    @staticmethod
    def mock_nothing():
        return MockingConfig(
            mock_spotify=False,
            mock_jingle_playback=False,
            simulate_waiting=False,
            begin_before_1st_job=None
        )


@dataclass
class Config:
    _ = KW_ONLY
    jingles: JingleConfig
    calendar: CalendarConfig
    mocking: MockingConfig
