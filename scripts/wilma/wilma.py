import os
from re import sub
import configparser

from scripts.general.cmd import *

BASE_COMMAND = '"C:\Program Files (x86)\Epic\Wilma\Epic.Release.Wilma.exe" env=TRACKAPPTCP '
#TODO: Verify if you can select by DLG via command prompt (likely you can)
#TODO: Verify if you can select timestamp via command prompt

def _is_valid_version(ver):
    #TODO - parse for a #.# format and check if it's less than the latest version?
    return ver
    
def _get_stream(ver, latestVersion):
    # Remove non-numerica characters to get stream.
    # (Exception 8.2 == 822 and 8.5 = 850) I doubht anyone cares about 8.2 and 8.5 is no longer available
    if ver == latestVersion:
        return "2"

    return sub(r'[^0-9]',"",ver)

class Wilma():
    """Wilma class"""

    def __init__(self, ver):
        # Config File
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(os.path.dirname(__file__),"..\config.ini")) # https://stackoverflow.com/questions/13800515/cant-load-relative-config-file-using-configparser-from-sub-directory
        self.latestVersion = self.config['Shared']['LatestVersion'] # TODO - centralize the API?

        if not ver:
            self.version = self.latestVersion
        else:
            self.version = _is_valid_version(ver)

    def _run(self, command, stream, status, product, logging, silent):
        """
        Runs Wilma command line for update/install given run parameters.
        """
        if not stream:
            stream = _get_stream(self.version, self.latestVersion)

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
