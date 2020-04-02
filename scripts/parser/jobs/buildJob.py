from .job import Job, Status
from datetime import datetime
from scripts.hsweb.build import HSWebBuild

BASE_DIRECTORY = ''

class HSWebBuildJob(Job):
    """Job configuration unique to HSWeb Builds"""
    
    def __init__(self, job, name, actions):
        super().__init__(name, actions)
        # Things unique to HSWebBuildJobs
        self.working_dir = BASE_DIRECTORY
        self.ver = '9.3' # Default to latest version #TODO - this needs to update with new releases
        self._parse_additional_attributes(job)
        self.hsweb = HSWebBuild(self.ver, self.working_dir)

        # Not ideal, but does the trick for now
        self.COMMANDS = {
            'clean' : self.hsweb.clean,
            'buildAll' : self.hsweb.build_all,
            'buildAllClean' : self.hsweb.build_all_clean,
            'buildCore' : self.hsweb.build_core,
            'buildCommon' : self.hsweb.build_common,
            'publish' : self.hsweb.publish,
            'build' : self._build
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
        report += '\nHSWebBuildJob details: TODO'
        return report

    def _parse_additional_attributes(self, job):
        try:
            self.working_dir += job.attrib['path']
            self.ver = job.attrib['ver']
        except KeyError:
            print('Invalid HSWebBuildJob attributes') #TODO better error handling
    
    def _build(self, **kwargs):
        try:
            solutions = kwargs['solutions']
        except KeyError:
            print('Invalid arguments passed to HSWeb build')
            return False

        return self.hsweb.build(**kwargs)
