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
# mocking.begin_before_1st_job = timedelta(seconds=5)
# mocking.simulate_waiting = True
# mocking = mocking.mock_everything()

calendar = CalendarConfig(
    calendar_url="https://calendar.google.com/calendar/ical/a8a96c310f25dc62b169b1de208393d93f8be47bedbeaff94d21f5fc9e3a5414%40group.calendar.google.com/public/basic.ics",
    calendar_file="fackelup.ics",
    download_calendar=True,
)

jingles = JingleConfig(
    jingles=[
        Jingle("Start", soundfile="fup24/start.mp3", offset="-30s"),
        Jingle("5 min left", soundfile="fup24/5min.mp3", offset="-5m", anchor="end"),
        Jingle("End", soundfile="fup24/end.mp3", anchor="end"),
    ]
)

config = Config(jingles=jingles, mocking=mocking, calendar=calendar)
