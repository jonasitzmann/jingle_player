import logging

import playsound  # modified so that jingles can be stopped!

from src import spotify


def play_sound(sound_path=None, mock=False):
    if mock:
        logging.info(f"playing sound file {sound_path}")
    else:
        playsound.playsound(sound_path, block=True)


def play_jingle_blocking(sound_path=None, mock_pytify=False, mock=False):
    sound_path = sound_path or "sound.mp3"
    with spotify.pause_spotify(mock_pytify, mock=mock):
        play_sound(sound_path, mock=mock)
