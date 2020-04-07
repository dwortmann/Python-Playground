import os
import time
import configparser

from scripts.general.cmd import *
from scripts.general.explorer import *

BASE_PATH = 'C:\EpicSource\{}\{}\HSWeb' #Requires major version + Directory
BUILD_COMMAND = 'C:\Epic\Tools\BuildSolution\\build-debug-solution.cmd "{}"'

class InvalidBuildCommandException(Exception):
    pass

def _is_valid_version(ver):
    #TODO - parse for a #.# format and check if it's less than the latest version?
    return ver

class HSWebBuild():
    """HSWeb build class"""

    def __init__(self, ver, branch):
        # Config File
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(os.path.dirname(__file__),"..\config.ini")) # https://stackoverflow.com/questions/13800515/cant-load-relative-config-file-using-configparser-from-sub-directory

        if not ver:
            self.version = self.config['Shared']['LatestVersion'] # TODO - centralize the API?
        else:
            self.version = _is_valid_version(ver)

        self.path = BASE_PATH.format(self.version, branch)

        try:
            is_valid_path(self.path)
        except InvalidPathException:
            print("***ERROR*** HSWebBuild Invalid Path " + self.path)
            # TODO - invalidated the job as well - in buildJob.py?

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
                print("***ERROR*** HSWebBuild Invalid Solution Path: " + solution)
                continue
            except FileNotFoundError:
                continue

            #BuildErr file is kept by the previous process - delay? (good enough)
            if not __debug__:
                time.sleep(1)

            command = BUILD_COMMAND.format(path)
            execute(command, timeout=1200)

        return True
