from datetime import timezone
import urllib.request
import pytz
from icalendar import Calendar
from parse_config import CalendarConfig

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


def main():
    calendar_url = 'https://calendar.google.com/calendar/ical/03ad48c1cf1d6a6a72575a04772c120c3c36be6849ab092f8ca0cce60a0cf9c3%40group.calendar.google.com/private-780b02e544d0d219d19aafe3ff3342cc/basic.ics'
    games = get_games(calendar_url, True)
    print('\n'.join([str(game) for game in games]))


if __name__ == '__main__':
    main()
