import os

from enum import Enum
from datetime import datetime

JOB_LOG_DIRECTORY = ''

class Status(Enum):
        """Track job status"""
        NotStarted = 1
        InProgress = 2
        Complete = 3
        Failed = 4

class Job:
    """Class to hold jobs from configuration file"""

    def __init__(self, name, actions):
        #Things needed for EVERY job
        self.name = name
        self.actions = actions
        self.status = Status.NotStarted
        self.start_time = None
        self.end_time = None

    def report(self):
        """Return a basic report about the status of the job"""
        report = '{} results\n'.format(self.name)
        report += 'Start time: {}\tEnd time: {}\n'.format(self.start_time, self.end_time)
        report += 'Status: {}\n'.format(self.status)
        report += str(self.actions)

        return report
    
    def log(self, content=None):
        if content is None:
            content = self.report()

        # Write content to file
        file_name = JOB_LOG_DIRECTORY + datetime.strftime(datetime.now(), '%Y%m%d.log')
        if os.path.exists(file_name):
            append_write = 'a' # append if already exists
        else:
            append_write = 'w' # make a new file if not

        f = open(file_name, append_write)
        f.write(content + '\n\n')
        f.close()

    def __str__(self):
        """String format"""
        return '\nName: {}\nStatus: {}\nActions: {}\n'.format(self.name ,self.status.name ,str(self.actions))

