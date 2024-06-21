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
mocking.begin_before_1st_job = timedelta(seconds=10)
# mocking.simulate_waiting = True
# mocking = mocking.mock_everything()

calendar = CalendarConfig(
    calendar_url="https://calendar.google.com/calendar/ical/eaac02f97eb073be209b33f0256f0eae6ab70c7d7989ea3f02b452cc91005f59%40group.calendar.google.com/public/basic.ics",
    calendar_file="mucho_gusto_cup.ics",
    download_calendar=True,
)

jingles = JingleConfig(
    jingles=[
        # Jingle("pre_game", offset="-3m", soundfile="pre_game.mp3"),
        Jingle("Start", soundfile="Start_Jingle.mp3", time_on_end=True),
        # Jingle("start", soundfile="ok_lets_go_remix.mp3", time_on_end=False),
        Jingle("5 min left", soundfile="5Minuten.mp3", offset="-5m", anchor="end"),
        Jingle("End", soundfile="Outro_Jingle.mp3", anchor="end"),
    ]
)

config = Config(jingles=jingles, mocking=mocking, calendar=calendar)
