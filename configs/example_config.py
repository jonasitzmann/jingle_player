from src.config import (
    Config,
    MockingConfig,
    CalendarConfig,
    JingleConfig,
    Jingle,
    timedelta,
)

mocking = (
    MockingConfig.mock_nothing()
)  # debugging options (e.g. simulate time, don't play sound, don't access spotify)
mocking.begin_before_1st_job = timedelta(seconds=5)

calendar = CalendarConfig(
    calendar_url="https://calendar.google.com/calendar/ical/03ad48c1cf1d6a6a72575a04772c120c3c36be6849ab092f8ca0cce60a0cf9c3%40group.calendar.google.com/private-780b02e544d0d219d19aafe3ff3342cc/basic.ics",
    calendar_file="../schedule.ics",
    download_calendar=True,
)

jingles = JingleConfig(
    jingles=[
        Jingle("pre_game", offset="-3m", soundfile="pre_game.mp3"),
        # Jingle('pre_game_5s', offset='-5s', soundfile='start_minus_5s.mp3'),
        Jingle("start"),  # soundfile not needed if it matches the jingle name
        Jingle("pre_end", offset="-5m", anchor="end"),
        Jingle("end", anchor="end"),
    ]
)

config = Config(jingles=jingles, mocking=mocking, calendar=calendar)
