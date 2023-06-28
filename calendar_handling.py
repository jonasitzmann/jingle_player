import urllib.request
from datetime import timezone

import pytz
from icalendar import Calendar

from config import CalendarConfig
from datastructures import Game


def get_games_from_calendar(calendar: Calendar, tz: timezone=None):
    tz = tz or pytz.timezone('Europe/Berlin')
    games = []
    for component in calendar.walk('VEVENT'):
        event_start = component.get('DTSTART').dt.astimezone(tz)
        event_end = component.get('DTEND').dt.astimezone(tz)
        event_name = component.get('SUMMARY')
        games.append(Game(start=event_start, end=event_end, name=event_name))
    return games


def load_calendar(ical_file='schedule.ics'):
    with open(ical_file, 'rb') as file:
        content = file.read()
    calendar = Calendar.from_ical(content)
    return calendar


def download_calendar(calendar_url=None, ical_file='schedule.ics'):
    urllib.request.urlretrieve(calendar_url, ical_file)
    return load_calendar(ical_file)


def get_games(calendar_url, calendar_file, download=True, tz=None):
    if download:
        calendar = download_calendar(calendar_url=calendar_url, ical_file=calendar_file)
    else:
        calendar = load_calendar(ical_file=calendar_file)
    games = get_games_from_calendar(calendar, tz=tz)
    return games


def get_games_from_cfg(cfg: CalendarConfig):
    return get_games(
        calendar_url=cfg.calendar_url,
        calendar_file=cfg.calendar_file,
        download=cfg.download_calendar
    )
