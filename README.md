# Jingle Player

This is a Python script for scheduling and playing jingles based on a calendar of games.

[![Video](https://img.youtube.com/vi/VPrawxp-m2Q/maxresdefault.jpg)](https://www.youtube.com/watch?v=VPrawxp-m2Q)
# Requirements

Python 3.x
External libraries: `pandas`, `playsound`, `pytz`, `freezegun`, `icalendar`, `pytify`, `pytimeparse`
# Installation

Clone the repository or download the script file.
Install the required external libraries using `pip`:
```
pip install pandas playsound pytz freezegun icalendar pytify pytimeparse
```
# Configuration

To configure the script, modify the example config file `config.py`. Adjust the settings for jingles, calendar, and mocking according to your needs.

Calendar Configuration
The script supports two ways of providing the game calendar:

Calendar URL: You can specify the URL of an iCalendar file in the `calendar_url` field of the `CalendarConfig` object. The script will download the calendar from the specified URL and save it locally.

Local Calendar File: Alternatively, you can provide a local iCalendar file by specifying the file path in the `calendar_file` field of the `CalendarConfig` object. The script will load the calendar directly from the local file.

Ensure that you set the `download_calendar` flag accordingly to choose whether to download the calendar from the URL or use the local file.



## Mocking Options
The script provides mocking options for debugging purposes. You can customize the behavior by modifying the mocking object in the configuration.
- `mock_spotify`: Set to `True` to mock Spotify-related functionality. Set to `False` to use the actual Spotify integration.
- `mock_jingle_playback`: Set to `True` to mock jingle playback. Set to `False` to play the jingles using the sound system.
- `simulate_waiting`: Set to `True` to simulate waiting between job executions. Set to `False` for real-time execution.
- `begin_before_1st_job`: Set a `timedelta` value to specify the time to begin before the first scheduled job. Set to `None` to start at the acutual current time.

# Running the Script

To run the script, execute the following command:

```
python script.py [--config CONFIG_FILE]
```

`--config` (optional): Specify the path to a Python config file to override the default configuration.

## Example output
```
Sat 09:27:48 starting jingle player
Sat 09:27:58 executing job Pool A - Match 1: start
Sat 09:27:58 playing sound file jingles/ok_lets_go_remix.mp3
Sat 10:10:00 executing job Pool A - Match 1: pre_end
Sat 10:10:00 playing sound file jingles/pre_end.mp3
Sat 10:15:00 executing job Pool A - Match 1: end
Sat 10:15:00 playing sound file jingles/end.mp3
Sat 10:27:58 executing job Pool B - Match 1: start
Sat 10:27:58 playing sound file jingles/ok_lets_go_remix.mp3
Sat 11:10:00 executing job Pool B - Match 1: pre_end
Sat 11:10:00 playing sound file jingles/pre_end.mp3
Sat 11:15:00 executing job Pool B - Match 1: end
Sat 11:15:00 playing sound file jingles/end.mp3
Sat 11:17:58 executing job Pool A - Match 2: start
Sat 11:17:58 playing sound file jingles/ok_lets_go_remix.mp3
Sat 12:00:00 executing job Pool A - Match 2: pre_end
Sat 12:00:00 playing sound file jingles/pre_end.mp3
Sat 12:05:00 executing job Pool A - Match 2: end
Sat 12:05:00 playing sound file jingles/end.mp3
Sat 12:07:58 executing job Pool B - Match 2: start
Sat 12:07:58 playing sound file jingles/ok_lets_go_remix.mp3
Sat 12:50:00 executing job Pool B - Match 2: pre_end
Sat 12:50:00 playing sound file jingles/pre_end.mp3
Sat 12:55:00 executing job Pool B - Match 2: end
Sat 12:55:00 playing sound file jingles/end.mp3
[...]
Sun 08:57:58 executing job 6A6B, 1A1B: start
Sun 08:57:58 playing sound file jingles/ok_lets_go_remix.mp3
Sun 09:40:00 executing job 6A6B, 1A1B: pre_end
Sun 09:40:00 playing sound file jingles/pre_end.mp3
Sun 09:45:00 executing job 6A6B, 1A1B: end
Sun 09:45:00 playing sound file jingles/end.mp3
Sun 09:57:58 executing job Crossovers: start
Sun 09:57:58 playing sound file jingles/ok_lets_go_remix.mp3
Sun 10:40:00 executing job Crossovers: pre_end
Sun 10:40:00 playing sound file jingles/pre_end.mp3
Sun 10:45:00 executing job Crossovers: end
Sun 10:45:00 playing sound file jingles/end.mp3
Sun 11:17:58 executing job Semis 5-12: start
Sun 11:17:58 playing sound file jingles/ok_lets_go_remix.mp3
Sun 12:00:00 executing job Semis 5-12: pre_end
Sun 12:00:00 playing sound file jingles/pre_end.mp3
Sun 12:05:00 executing job Semis 5-12: end
Sun 12:05:00 playing sound file jingles/end.mp3
Sun 12:17:58 executing job Semis 1-4: start
Sun 12:17:58 playing sound file jingles/ok_lets_go_remix.mp3
Sun 13:00:00 executing job Semis 1-4: pre_end
Sun 13:00:00 playing sound file jingles/pre_end.mp3
Sun 13:05:00 executing job Semis 1-4: end
Sun 13:05:00 playing sound file jingles/end.mp3
Sun 13:07:58 executing job Placement 5-12: start
Sun 13:07:58 playing sound file jingles/ok_lets_go_remix.mp3
Sun 13:50:00 executing job Placement 5-12: pre_end
Sun 13:50:00 playing sound file jingles/pre_end.mp3
Sun 13:55:00 executing job Placement 5-12: end
Sun 13:55:00 playing sound file jingles/end.mp3
Sun 13:57:58 executing job Place 3: start
Sun 13:57:58 playing sound file jingles/ok_lets_go_remix.mp3
Sun 14:22:58 executing job Final: start
Sun 14:22:58 playing sound file jingles/ok_lets_go_remix.mp3
Sun 14:40:00 executing job Place 3: pre_end
Sun 14:40:00 playing sound file jingles/pre_end.mp3
Sun 14:45:00 executing job Place 3: end
Sun 14:45:00 playing sound file jingles/end.mp3
Sun 15:05:00 executing job Final: pre_end
Sun 15:05:00 playing sound file jingles/pre_end.mp3
Sun 15:10:00 executing job Final: end
Sun 15:10:00 playing sound file jingles/end.mp3
```

# License

This script is released under the MIT License.

Feel free to modify and use it according to your needs. Contributions and suggestions are welcome!
