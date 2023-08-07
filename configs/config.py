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
# mocking.begin_before_1st_job = timedelta(seconds=5)  #  uncomment to start just before 1st jingle
# mocking.simulate_waiting = True  # uncomment this to fast-forward in time

calendar = CalendarConfig(
    calendar_url="https://calendar.google.com/calendar/ical/e6f512a5ddca7b07fae3ba0f7ef1eee936f1ac879d9e270ef8c228286fa1900d%40group.calendar.google.com/public/basic.ics",
    calendar_file="../schedule.ics",
    download_calendar=True,  # set to false for offline use (with ical file)
)

jingles = JingleConfig(
    jingles=[
        Jingle("start", soundfile="start.mp3"),
        Jingle("pre_end", offset="-5m", anchor="end", soundfile="pre_end.mp3"),
        Jingle("end", anchor="end", soundfile="end.mp3"),
    ]
)

config = Config(jingles=jingles, mocking=mocking, calendar=calendar)
