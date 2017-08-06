from .job import Job
from epic.svn.commands import SVN

class SVNJob(Job):
    """Job configuration unique to SVN"""

    def __init__(self, name, actions):
        super().__init__(name, actions)
        print('SVNJob __init__')
        #Things unique to SVN Jobs

    def update(self):
        SVN.update()

    def checkout(self):
        SVN.checkout()

    def revert(self):
        SVN.revert()

    def cleanup(self):
        SVN.cleanup()










