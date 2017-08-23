from .job import Job, Status
from datetime import datetime
from scripts.svn.commands import SVN

BASE_DIRECTORY = ''

class SVNJob(Job):
    """Job configuration unique to SVN"""

    def __init__(self, job, name, actions):
        super().__init__(name, actions)
        #Things unique to SVN Jobs
        self.working_dir = BASE_DIRECTORY
        self._parse_additional_attributes(job)

        # Not ideal, but does the trick for now
        self.COMMANDS = {
            'update' : self._update,
            'checkout' : self._checkout,
            'revert' : self._revert,
            'cleanup' : self._cleanup
        }

    def run(self, log=True, email=True):
        """
        Run job and all it's actions
        
        :param log: Whether to log job and actions in nightly log
        :param email: Whether to send log email for job.
        """
        self.start_time = datetime.now()
        self.status = Status.InProgress

        for action in self.actions:
            command = action[0]
            params = action[1]
            # Execute actions
            try:
                status = self.COMMANDS[command](**params)
                if not status:
                    self.status = Status.Failed
                    print('Action failed to execute')
            except TypeError:
                self.status = Status.Failed
                print('Invalid job or parameter') #TODO, better error handling

        # Do report/email stuff after this
        if self.status != Status.Failed:
            self.status = Status.Complete

        self.end_time = datetime.now()

    def report(self):
        """Return a basic report about SVN job status"""
        report = super().report()
        report += '\nSVNJob details: TODO'
        return report

    def _parse_additional_attributes(self, job):
        try:
            self.working_dir += job.attrib['path']
        except KeyError:
            print('Invalid SVNJob attributes') #TODO better error handling

    def _update(self, **kwargs):
        return SVN.update(self.working_dir, **kwargs)

    def _checkout(self, **kwargs):
        return SVN.checkout(self.working_dir, **kwargs)

    def _revert(self, **kwargs):
        return SVN.revert(self.working_dir, **kwargs)

    def _cleanup(self):
        return SVN.cleanup(self.working_dir)
