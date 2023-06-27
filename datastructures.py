import datetime
from dataclasses import dataclass


@dataclass
class Game:
    start: datetime.datetime
    end: datetime.datetime
    name: str

    def __str__(self):
        weekday = self.start.strftime('%A')
        start = self.start.strftime('%H:%M')
        end = self.end.strftime('%H:%M')
        return f'Game: {self.name} on {weekday} from {start} to {end}'