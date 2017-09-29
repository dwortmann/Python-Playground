import sys
import time
import subprocess

# There's a bug running commands in windows shell where the last line isn't recognized.
# Keeping this list allows us to press <Enter> at the proper time.
BUILD_CMD_PROMPTS = [
    'All done', 'Errors in build', 'Press any key to continue'
]

def execute(cmd, timeout=600):
    """
    Execute a command in windows shell.
    
    TODO: Expect prompts as parameter - if we need this...
    """
    if __debug__:
        print('***DEBUG*** Command: ' + cmd)
        return

    p = subprocess.Popen(cmd, shell=True, \
            stdout=subprocess.PIPE, \
            stdin=subprocess.PIPE, \
            stderr=subprocess.STDOUT, \
            bufsize=1, universal_newlines=True)

    start_time = time.time()
    end_time = start_time + timeout

    while p.poll() is None:
        if time.time() > end_time:
            p.kill()
            # TODO: integrate a logger
            print('***WARNING*** Command timeout exceeded!')
            print('***WARNING*** Command: ' + cmd)
            break;

        line = p.stdout.readline()
        try:
            # Workaround for expecter bug in windows shell
            for prompt in BUILD_CMD_PROMPTS:
                if line.startswith(prompt):
                    p.communicate('\r\n')

            print(line, end='') #TODO - consider ways to log this/debug mode?
        except TypeError:
            pass