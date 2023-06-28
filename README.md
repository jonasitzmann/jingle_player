# Game Scheduler

This is a Python script for scheduling and playing jingles based on a calendar of games.

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
# License

This script is released under the MIT License.

Feel free to modify and use it according to your needs. Contributions and suggestions are welcome!