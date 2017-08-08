from .job import Job
from scripts.svn.commands import SVN

class SVNJob(Job):
    """Job configuration unique to SVN"""

    def __init__(self, name, actions):
        super().__init__(name, actions)
        print('SVNJob __init__')
        #Things unique to SVN Jobs

    def update(self, path, revision=None):
        SVN.update(path, revision)

    def checkout(self, path, revision=None):
        SVN.checkout(path, revision)

    def revert(self):
        SVN.revert()

    def cleanup(self):
        SVN.cleanup()










