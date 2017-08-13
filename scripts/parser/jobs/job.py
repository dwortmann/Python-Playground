from enum import Enum

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

    def report(self):
        """Return a basic report about the status of the job"""
        return 'Basic Job report ' + str(self.status)
        
    def __str__(self):
        """String format"""
        return '\nName: {}\nStatus: {}\nActions: {}\n'.format(self.name ,self.status.name ,str(self.actions))

