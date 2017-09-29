import subprocess

def execute(cmd):
    """
    Execute a command in windows shell.
    
    TODO: Expect prompts as parameter
    """
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