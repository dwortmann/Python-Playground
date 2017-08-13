from .job import Job
from scripts.svn.commands import SVN

class SVNJob(Job):
    """Job configuration unique to SVN"""

    def __init__(self, job, name, actions):
        super().__init__(name, actions)
        #Things unique to SVN Jobs
        print('SVNJob __init__')
        self._parse_additional_attributes(job)
        
    def run(self):
        """
        Run job and all it's actions
        """
        return
        
    def _parse_additional_attributes(self, job):
        try:
            working_dir = job.attrib['path']
        except KeyError:
            #TODO: error handling
            print('Invalid SVNJob attributes')

    def _update(self, path, revision=None):
        SVN.update(path, revision)

    def _checkout(self, path, revision=None):
        SVN.checkout(path, revision)

    def _revert(self):
        SVN.revert()
        
    def _cleanup(self):
        SVN.cleanup()










