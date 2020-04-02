from scripts.general.cmd import *

BASE_COMMAND = '"C:\Program Files (x86)\Epic\Wilma\Epic.Release.Wilma.exe" env=TRACKAPPTCP '
#TODO: Verify if you can select by DLG via command prompt (likely you can)
#TODO: Verify if you can select timestamp via command prompt

VERSIONS = ['9.3','9.2','9.1','8.9','8.8','8.7','8.6','8.5','8.4','8.3','8.2'] #TODO: Update with new versions
DEFAULT_STREAM = {
    '9.3' : '2',
    '9.2' : '92',
    '9.1' : '91',
    '8.9' : '89',
    '8.8' : '88',
    '8.7' : '87',
    '8.6' : '86',
    '8.5' : '850',
    '8.4' : '84',
    '8.3' : '83',
    '8.2' : '822',
}

def _is_valid_version(ver):
    if ver in VERSIONS:
        return ver
    else:
        return '8.9' #TODO, probably not ideal, but eh

class Wilma():
    """Wilma class"""

    def __init__(self, ver):
        self.version = _is_valid_version(ver)

    def _run(self, command, stream, status, product, logging, silent):
        """
        Runs Wilma command line for update/install given run parameters.
        """
        if not stream:
            stream = DEFAULT_STREAM[self.version]

        if logging:
            command += '-l '

        if silent:
            command += '-s '

        command += '-v {} -t {} -p {} '.format(stream, status, product)

        execute(command, timeout=1200)

    def update(self, stream=None, status='130', product="1", logging=True, silent=True):
        """
        Python wrapper for updating Wilma via command line.

        Reference: http://wiki.epic.com/main/Wilma#Running_Wilma_at_the_command_line
        """
        command = BASE_COMMAND + '-upd '

        self._run(command, stream, status, product, logging, silent)

        return True

    def install(self, stream=None, status='130', product="1", logging=True, silent=True):
        """
        Python wrapper for installing Wilma via command line.

        Reference: http://wiki.epic.com/main/Wilma#Running_Wilma_at_the_command_line
        """
        command = BASE_COMMAND

        self._run(command, stream, status, product, logging, silent)

        return True
