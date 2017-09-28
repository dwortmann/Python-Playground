import os
import time
import subprocess

BASE_COMMAND = '"C:\Program Files (x86)\Epic\\v{}\Wilma\Epic.Release.Wilma.exe" env=TRACKAPPTCP '
#TODO: Verify if you can select by DLG via command prompt (likely you can)
#TODO: Verify if you can select timestamp via command prompt

VERSIONS = ['8.4','8.3','8.2']
DEFAULT_STREAM = {
    '8.4' : '2',
    '8.3' : '83',
    '8.2' : '822',
}

class InvalidBuildCommandException(Exception):
    pass

def _execute(cmd):
    if __debug__:
        print(cmd)
        return

    p = subprocess.Popen(cmd, shell=True, \
            stdout=subprocess.PIPE, \
            stdin=subprocess.PIPE, \
            stderr=subprocess.STDOUT, \
            bufsize=1, universal_newlines=True)

    while p.poll() is None:
        line = p.stdout.readline()
        try:
            #TODO: implement a timeout for each command in case of error - 5 mins or so should be good
            if line.startswith('All done'):
                p.communicate('\r\n')
            if line.startswith('Errors in build'):
                p.communicate('\r\n')
            if line.startswith('Press any key to continue'):
                # Keep as backup
                p.communicate('\r\n')
            print(line, end='') #TODO - consider ways to log this/debug mode?
        except TypeError:
            pass

def _is_valid_version(ver):
    if ver in VERSIONS:
        return ver
    else:
        return '8.4' #TODO, probably not ideal, but eh

class Wilma():
    """Wilma class"""

    def __init__(self, ver):
        self.version = _is_valid_version(ver)

    def _run(self, command, stream, status, product, logging, silent):
        """
        Run's Wilma command line for update/install given run parameters.
        """
        if not stream:
            stream = DEFAULT_STREAM[self.version]

        if logging:
            command += '-l '

        if silent:
            command += '-s '

        command += '-v {} -t {} -p {} '.format(stream, status, product)

        _execute(command)

    def update(self, stream=None, status='130', product="1", logging=True, silent=True):
        """
        Python wrapper for updating Wilma via command line.

        Reference: http://wiki.epic.com/main/Wilma#Running_Wilma_at_the_command_line
        """
        command = BASE_COMMAND.format(self.version) + '-upd '

        self._run(command, stream, status, product, logging, silent)

        return True

    def install(self, stream=None, status='130', product="1", logging=True, silent=True):
        """
        Python wrapper for installing Wilma via command line.

        Reference: http://wiki.epic.com/main/Wilma#Running_Wilma_at_the_command_line
        """
        command = BASE_COMMAND.format(self.version)

        self._run(command, stream, status, product, logging, silent)

        return True
