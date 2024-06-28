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
# mocking.begin_before_1st_job = timedelta(seconds=10)
# mocking.simulate_waiting = True
# mocking = mocking.mock_everything()

calendar = CalendarConfig(
    calendar_url="https://calendar.google.com/calendar/ical/3f7484898e2b35496dbd4f3d7193bfb68a2f40602d7755a9cdbbc4e8fea18705%40group.calendar.google.com/public/basic.ics",
    calendar_file="xdm.ics",
    download_calendar=True,
)

jingles = JingleConfig(
    jingles=[
        Jingle("Start", soundfile="Start_Jingle.mp3", time_on_end=True),
        Jingle("5 min left", soundfile="5Minuten.mp3", offset="-5m", anchor="end"),
        Jingle("End", soundfile="Outro_Jingle.mp3", anchor="end"),
    ]
)

config = Config(jingles=jingles, mocking=mocking, calendar=calendar)
