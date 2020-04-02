import time

from scripts.general.cmd import *
from scripts.general.explorer import *

BASE_PATH = 'C:\EpicSource\{}\{}\HSWeb' #Requires major version + Directory
BUILD_COMMAND = 'C:\Epic\Tools\BuildSolution\\build-debug-solution.cmd "{}"'

VERSIONS = ['9.3','9.2','9.1','8.9','8.8','8.7','8.6','8.5','8.4','8.3','8.2'] #TODO - update with new releases

class InvalidBuildCommandException(Exception):
    pass

class InvalidPathException(Exception):
    pass

def _is_valid_version(ver):
    if ver in VERSIONS:
        return ver
    else:
        return '9.3' #TODO, probably not ideal, but eh - annoying with new versions...

class HSWebBuild():
    """HSWeb build class"""

    def __init__(self, ver, branch):
        self.version = _is_valid_version(ver)
        self.path = BASE_PATH.format(self.version, branch)
        if not is_valid_path(self.path):
            pass#raise InvalidPathException('Invalid path: ' + self.path)

    def clean(self):
        exe_path = self.path + '\BuildScripts'
        # Change directory (not sure why it doesn't work otherwise...)
        command = 'cd "{}" && {}'.format(exe_path,'clean.cmd')

        execute(command)

        return True

    def build_all_clean(self):
        exe_path = self.path + '\BuildScripts'
        # Change directory (not sure why it doesn't work otherwise...)
        command = 'cd "{}" && {}'.format(exe_path,'build-all-CLEAN-debug.cmd')

        execute(command)

        return True

    def build_all(self):
        exe_path = self.path + '\BuildScripts'
        # Change directory (not sure why it doesn't work otherwise...)
        command = 'cd "{}" && {}'.format(exe_path,'build-all-Debug.cmd')

        execute(command)

        return True

    def build_core(self):
        exe_path = self.path + '\BuildScripts'
        # Change directory (not sure why it doesn't work otherwise...)
        command = 'cd "{}" && {}'.format(exe_path,'build-Core-Debug.cmd')

        execute(command)

        return True

    def build_common(self):
        exe_path = self.path + '\BuildScripts'
        # Change directory (not sure why it doesn't work otherwise...)
        command = 'cd "{}" && {}'.format(exe_path,'build-Common-Debug.cmd')

        execute(command)

        return True

    def publish(self):
        exe_path = self.path + '\BuildScripts'
        # Change directory (not sure why it doesn't work otherwise...)
        command = 'cd "{}" && {}'.format(exe_path,'publish-LOCALHOST.cmd')

        execute(command)

        return True

    def _valid_solution_path(self, solution):
        path = self.path + '\Solutions'
        # Search recursively for file
        solution_path = find_file(solution, path)

        if solution_path:
            return solution_path
        else:
            raise InvalidPathException

    def build(self, solutions):
        #Build all solutions passed in
        for solution in solutions.split():
            try:
                path = self._valid_solution_path(solution)
            except InvalidPathException:
                continue
            except FileNotFoundError:
                continue

            #TODO - BuildErr file is kept by the previous process - delay? Or do something more robust to wait until availalbe? (could be prone to getting stuck... )
            if not __debug__:
                time.sleep(1)

            command = BUILD_COMMAND.format(path)
            execute(command, timeout=1200)

        return True
