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
    calendar_url="https://calendar.google.com/calendar/ical/7541b5a95e60b93a9a619c028b86cc265688d859ef9e30979bfbdd7d57ffd5c9%40group.calendar.google.com/private-b0728355558f9928374e947875f8623e/basic.ics",
    calendar_file="fackelup.ics",
    download_calendar=True,
)

jingles = JingleConfig(
    jingles=[
        Jingle("Start", soundfile="fup25/start.mp3"),
        Jingle("5 min left", soundfile="fup25/5_min.mp3", offset="-5m", anchor="end"),
        Jingle("End", soundfile="fup25/end.mp3", anchor="end"),
    ]
)

config = Config(jingles=jingles, mocking=mocking, calendar=calendar)
