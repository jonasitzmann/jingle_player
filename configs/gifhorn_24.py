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
    calendar_url="https://calendar.google.com/calendar/ical/944deae1cbfb7842c01f6bacaeef5c03ae8be4c1037fd5d01ce2143ef15ddaba%40group.calendar.google.com/public/basic.ics",
    calendar_file="gifhorn_24.ics",
    download_calendar=True,
)

jingles = JingleConfig(
    jingles=[
        Jingle("Start", soundfile="gifhorn_24/start.mp3", offset="-30s"),
        Jingle("5 min left", soundfile="gifhorn_24/5min.mp3", offset="-5m", anchor="end"),
        Jingle("End", soundfile="gifhorn_24/end.mp3", anchor="end"),
    ]
)

config = Config(jingles=jingles, mocking=mocking, calendar=calendar)
