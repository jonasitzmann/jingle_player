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
    calendar_url="https://calendar.google.com/calendar/ical/734a4357b947c75cb33fa845522d63f5b4dd36b5f1225721bd021418ada300ea%40group.calendar.google.com/private-4d73fdab1dd47c7f620888ecd762de25/basic.ics",
    calendar_file="sturmfrei/schedule.ics",
    download_calendar=True,  # set to false for offline use (with ical file)
)

jingles = JingleConfig(
    jingle_dir='sturmfrei',
    jingles=[
        Jingle("start", soundfile="start_jingle.mp3"),
        Jingle("2 min. left", offset="-2m", anchor="end", soundfile="2_minutes_left_jingle.mp3"),
        Jingle("end", anchor="end", soundfile="end_jingle.mp3"),
    ]
)

config = Config(jingles=jingles, mocking=mocking, calendar=calendar)
