from .job import Job
from scripts.svn.commands import SVN

class SVNJob(Job):
    """Job configuration unique to SVN"""

    def __init__(self, job, name, actions):
        super().__init__(name, actions)
        #Things unique to SVN Jobs
        print('SVNJob __init__')
        self._parse_additional_attributes(job)
        
    def _parse_additional_attributes(self, job):
        try:
            working_dir = job.attrib['path']
        except KeyError:
            #TODO: error handling
            print('Invalid SVNJob attributes')

    def update(self, path, revision=None):
        SVN.update(path, revision)

    def checkout(self, path, revision=None):
        SVN.checkout(path, revision)

    def revert(self):
        SVN.revert()










