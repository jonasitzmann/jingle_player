import enum
import logging
import time
from datetime import datetime, timedelta
from functools import partial
from humanize import naturaldelta

import pandas as pd
import pytz
from freezegun import freeze_time
from reprint import output


def ljust(s):
    s = s.astype(str).str.strip()
    return s.str.ljust(s.str.len().max())


class JobAttr(enum.Enum):
    func = "func"
    date = "scheduled at"
    id = "id"
    name = "jingle name"
    time_left = "time left"


job_formatters = {JobAttr.func.name: lambda func: func.__name__}


class Scheduler:
    def __init__(self, tz=None, job_timeout=None):
        self.jobs = pd.DataFrame(
            columns=[
                JobAttr.func,
                JobAttr.date,
                JobAttr.id,
                JobAttr.name,
                JobAttr.time_left,
            ]
        )
        self.jobs[JobAttr.date] = pd.to_datetime(self.jobs[JobAttr.date])
        self.tz = tz if tz is not None else pytz.timezone("Europe/London")
        self.job_timeout = (
            job_timeout if job_timeout is not None else timedelta(seconds=5)
        )
        self.job_timeout = self.job_timeout.total_seconds()
        self.output_lines = None

    def now(self):
        return datetime.now(tz=self.tz)

    def add_job(self, func, date, job_id, name=None):
        name = name or job_id
        job = {
            JobAttr.func: func,
            JobAttr.date: date,
            JobAttr.id: job_id,
            JobAttr.name: name,
        }
        self.jobs = self.jobs._append(job, ignore_index=True)

    def get_due_jobs(self):
        now = self.now()
        self.jobs[JobAttr.time_left] = (
            self.jobs[JobAttr.date].apply(lambda x: x.timestamp()) - now.timestamp()
        )
        due_jobs = self.jobs[self.jobs[JobAttr.time_left] <= 0]
        timed_out_jobs, due_jobs = (
            due_jobs[timeout_mask := due_jobs[JobAttr.time_left] < (-self.job_timeout)],
            due_jobs[~timeout_mask],
        )
        return due_jobs, timed_out_jobs

    def get_reprint_output(self):
        first_output = self.get_output_lines()
        out = output(initial_len=len(first_output), interval=0)
        return out

    def get_output_lines(self):
        dateformat = "%a %H:%M:%S"
        df = self.jobs.copy()[[JobAttr.name, JobAttr.time_left, JobAttr.date]]
        df.sort_values(JobAttr.time_left, inplace=True)
        df[JobAttr.time_left] = df[JobAttr.time_left].apply(naturaldelta)
        df[JobAttr.date] = df[JobAttr.date].apply(lambda x: x.strftime(dateformat))
        df.columns = [c.value for c in df.columns]
        out_str = df.apply(ljust).to_string(index=False, justify="left")
        first_line = f"Current time: {(datetime.now(tz=self.tz) + timedelta(hours=1)).strftime(dateformat)}"
        out_str = f"\n \n{first_line}\n \n{out_str}"
        return out_str.splitlines()[:20]

    def _main_loop(self, wait_fn=None):
        logging.info("starting jingle player")
        wait_fn = wait_fn or partial(time.sleep, 1)
        with self.get_reprint_output() as out:
            while not self.jobs.empty:
                due_jobs, timed_out_jobs = self.get_due_jobs()
                for _, job in due_jobs.iterrows():
                    logging.info(f"executing job {job[JobAttr.name]}")
                    job[JobAttr.func]()
                    self.jobs = self.jobs[
                        self.jobs[JobAttr.id] != job[JobAttr.id]
                    ]  # pop job
                for _, job in timed_out_jobs.iterrows():
                    logging.warning(f"job {job[JobAttr.name]} reached timeout")
                    self.jobs = self.jobs[
                        self.jobs[JobAttr.id] != job[JobAttr.id]
                    ]  # pop job
                out.change(self.get_output_lines())
                wait_fn()

    def main_loop_simulated(
        self, simulate_waiting: bool, begin_before_1st_job: timedelta
    ):
        start_date = datetime.now(tz=self.tz)
        if begin_before_1st_job is not None:
            start_date = self.jobs[JobAttr.date].min() - begin_before_1st_job

        with freeze_time(start_date, tick=not simulate_waiting) as frozen_time:
            dt = timedelta(seconds=1)
            wait_fn = (
                partial(frozen_time.tick, dt)
                if simulate_waiting
                else partial(time.sleep, 1)
            )
            self._main_loop(wait_fn=wait_fn)

    def main_loop(self, simulate_waiting, begin_before_1st_job):
        if (begin_before_1st_job is not None) or simulate_waiting:
            return self.main_loop_simulated(
                simulate_waiting=simulate_waiting,
                begin_before_1st_job=begin_before_1st_job,
            )
        else:
            return self._main_loop()
