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
mocking.begin_before_1st_job = timedelta(seconds=3)
# mocking.simulate_waiting = True
# mocking = mocking.mock_everything()

calendar = CalendarConfig(
    calendar_url="https://calendar.google.com/calendar/ical/10bd08c5ab7527e9d00dc60572cd11a83bdd0acd2d6791274d1b3426e401e0b8%40group.calendar.google.com/public/basic.ics",
    calendar_file="fackelup.ics",
    download_calendar=True,
)

jingles = JingleConfig(
    jingles=[
        Jingle("Start", soundfile="start_23.mp3"),
        Jingle("5 min left", soundfile="5_min_23.mp3", offset="-5m", anchor="end"),
        Jingle("End", soundfile="end_23.mp3", anchor="end"),
    ]
)

config = Config(jingles=jingles, mocking=mocking, calendar=calendar)
