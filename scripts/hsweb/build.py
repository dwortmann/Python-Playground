import os
import subprocess

BASE_PATH = 'C:\EpicSource\{}\{}\HSWeb' #Requires major version + Directory
BUILD_COMMAND = 'C:\Epic\Tools\BuildSolution\build-debug-solution.cmd "{}"'

VERSIONS = ['8.4','8.3','8.2']

class InvalidBuildCommandException(Exception):
    pass

class InvalidPathException(Exception):
    pass

def _execute(cmd):
    p = subprocess.Popen(cmd, shell=True, \
            stdout=subprocess.PIPE, \
            stderr=subprocess.STDOUT)
    output, stderr = p.communicate()

    return output, stderr

def _is_valid_path(path, create_if_needed=False):
    """
    Verify the path either exists or can be created.

    :param path: relative path
    """
    if os.path.isdir(path):
        return True
    else:
        return False

def _is_valid_version(ver):
    if ver in VERSIONS:
        return ver
    else:
        return '8.4' #TODO, probably not ideal, but eh

class HSWebBuild():
    """HSWeb build class"""

    def __init__(self, ver, branch):
        self.version = _is_valid_version(ver)
        self.path = BASE_PATH.format(self.version, branch)
        if not _is_valid_path(self.path):
            raise InvalidPathException('Invalid path: ' + self.path)

    def clean(self):
        exe_path = self.path + '\BuildScripts'
        # Change directory (not sure why it doesn't work otherwise...)
        command = 'cd "{}" && {}'.format(exe_path,'clean.cmd')

        print(command)
        _execute(command)

    def build_all_clean(self):
        exe_path = self.path + '\BuildScripts'
        # Change directory (not sure why it doesn't work otherwise...)
        command = 'cd "{}" && {}'.format(exe_path,'build-all-CLEAN-debug.cmd')

        print(command)
        _execute(command)

    def build_all(self):
        exe_path = self.path + '\BuildScripts'
        # Change directory (not sure why it doesn't work otherwise...)
        command = 'cd "{}" && {}'.format(exe_path,'build-all-Debug.cmd')

        print(command)
        _execute(command)

    def build_core(self):
        exe_path = self.path + '\BuildScripts'
        # Change directory (not sure why it doesn't work otherwise...)
        command = 'cd "{}" && {}'.format(exe_path,'build-Core-Debug.cmd')

        print(command)
        _execute(command)

    def build_common(self):
        exe_path = self.path + '\BuildScripts'
        # Change directory (not sure why it doesn't work otherwise...)
        command = 'cd "{}" && {}'.format(exe_path,'build-Common-Debug.cmd')

        print(command)
        _execute(command)

    def publish(self):
        exe_path = self.path + '\BuildScripts'
        # Change directory (not sure why it doesn't work otherwise...)
        command = 'cd "{}" && {}'.format(exe_path,'publish-LOCALHOST.cmd')

        print(command)
        _execute(command)

    def _valid_solution_path(self, solution):
        path = self.path + '\Solutions'
        # Search recursively for file
        solution_path = self._valid_solution_path_recursive(solution, path)

        if solution_path:
            return solution_path
        else:
            raise InvalidPathException

    def _valid_solution_path_recursive(self, solution, path):
        solution_path = None
        dir_contents = os.listdir(path)

        # Check if solution in this directory
        try:
            idx = dir_contents.index(solution)
            return '{}\{}'.format(path, dir_contents[idx])
        except ValueError:
            #Not in this directory
            pass

        # Check any subdirectories
        for d in dir_contents:
            if not os.path.isdir('{}\{}'.format(path, d)):
                continue

            solution_path = self._valid_solution_path_recursive(solution, '{}\{}'.format(path, d))
            if solution_path:
                return solution_path

        return solution_path

    def build(self, *args):
        #Build all solutions passed in
        #TODO - is there a smarter way to just build all solutions with 1 command? SolutionsToBuild.sln?

        for solution in args:
            #TODO - search Apps and Fnd recursively here for the solution
            try:
                path = self._valid_solution_path(solution)
            except InvalidPathException:
                continue

            command = BUILD_COMMAND.format(path)
            print(command)
            #_execute(command)
