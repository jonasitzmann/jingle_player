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
# mocking.begin_before_1st_job = timedelta(minutes=5)
# mocking = mocking.mock_everything()

calendar = CalendarConfig(
    calendar_url="https://calendar.google.com/calendar/ical/56b5bd48fab0022a1a8a5937a8e00f29bdb68145551b1d7bf9646b9e24c03202%40group.calendar.google.com/public/basic.ics",
    calendar_file="mucho_gusto_cup.ics",
    download_calendar=True,
)

jingles = JingleConfig(
    jingles=[
        # Jingle("pre_game", offset="-3m", soundfile="pre_game.mp3"),
        # Jingle("start", soundfile="ok_lets_go_remix.mp3", time_on_end=True),
        Jingle("start", soundfile="ok_lets_go_remix.mp3", time_on_end=False),
        Jingle("pre_end", offset="-5m", anchor="end"),
        Jingle("end", anchor="end"),
    ]
)

config = Config(jingles=jingles, mocking=mocking, calendar=calendar)
