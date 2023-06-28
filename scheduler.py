from datetime import datetime, timedelta
import enum
import pandas as pd
import pytz
import logging
import time
from functools import partial
from freezegun import freeze_time


class JobAttr(enum.Enum):
    func = 'func'
    date = 'date'
    id = 'id'
    name = 'name'


class Scheduler:
    def __init__(self, tz=None):
        self.jobs = pd.DataFrame(columns=[JobAttr.func, JobAttr.date, JobAttr.id, JobAttr.name])
        self.jobs[JobAttr.date] = pd.to_datetime(self.jobs[JobAttr.date])
        self.tz = tz if tz is not None else pytz.timezone('Europe/London')

    def now(self):
        return datetime.now(tz=self.tz)

    def add_job(self, func, date, id, name=None):
        name = name or id
        job = {JobAttr.func: func, JobAttr.date: date, JobAttr.id: id, JobAttr.name: name}
        self.jobs = self.jobs._append(job, ignore_index=True)

    def get_due_jobs(self):
        now = self.now()
        due_jobs = self.jobs[self.jobs[JobAttr.date] <= now]
        return due_jobs

    def _main_loop(self, wait_fn=None):
        logging.info('starting jingle player')
        wait_fn = wait_fn or partial(time.sleep, 1)
        while not self.jobs.empty:
            due_jobs = self.get_due_jobs()
            for _, job in due_jobs.iterrows():
                logging.info(f'executing job\t{job[JobAttr.name]}')
                job[JobAttr.func]()
                self.jobs = self.jobs[self.jobs[JobAttr.id] != job[JobAttr.id]]  # pop job
            wait_fn()

    def main_loop_simulated(self, simulate_waiting: bool, begin_before_1st_job: timedelta):
        start_date = datetime.now(tz=self.tz)
        if begin_before_1st_job is not None:
            start_date = self.jobs[JobAttr.date].min() - begin_before_1st_job

        with freeze_time(start_date, tick=not simulate_waiting) as frozen_time:
            dt = timedelta(minutes=1)
            wait_fn = partial(frozen_time.tick, dt) if simulate_waiting else partial(time.sleep, 1)
            self._main_loop(wait_fn=wait_fn)

    def main_loop(self, simulate_waiting, begin_before_1st_job):
        if (begin_before_1st_job is not None) or simulate_waiting:
            return self.main_loop_simulated(simulate_waiting=simulate_waiting, begin_before_1st_job=begin_before_1st_job)
        else:
            return self._main_loop()
