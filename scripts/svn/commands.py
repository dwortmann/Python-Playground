import subprocess

def _execute(cmd):
    p = subprocess.Popen(cmd, shell=True, \
            stdout=subprocess.PIPE, \
            stderr=subprocess.STDOUT)
    output, stderr = p.communicate()

    return output, stderr
    
def _is_valid_path(path):
    return False #TODO

def _format_path(path):
    return path #TODO - also check if it's a valid path and such

def _is_valid_revision(rev):
    if not rev:
        return False
    if isinstance(rev, int):
        if rev > 0:
            return True
    if isinstance(rev, str):
        if rev.isdigit():
            return True

    return False

def _format_revision(rev):
    return str(rev).lstrip('0')

class SVN():
    """SVN commands object"""

    @staticmethod
    def update(path, rev=None):
        cmd = 'svn update '
        if _is_valid_revision(rev):
            cmd += '-r {} '.format(_format_revision(rev))
        cmd += '"{}"'.format(_format_path(path))

        print(cmd)
        _execute(cmd)

    @staticmethod
    def checkout(path, rev=None):
        cmd = 'svn checkout '
        if _is_valid_revision(rev):
            cmd += '-r {} '.format(_format_revision(rev))
        cmd += '"{}"'.format(_format_path(path))

        print(cmd)
        _execute(cmd)

    @staticmethod
    def revert():
        print('SVN Revert')

    @staticmethod
    def cleanup():
        print('SVN Cleanup')

    @staticmethod
    def merge():
        print('SVN Merge')

    @staticmethod
    def delete():
        print('SVN delete')

    @staticmethod
    def add():
        print('SVN add')

    @staticmethod
    def undo_add():
        print('SVN undo add')

    @staticmethod
    def commit():
        print('SVN commit')

    @staticmethod
    def unlock():
        print('SVN unlock')

    @staticmethod
    def show_log():
        print('SVN show log')

    @staticmethod
    def diff():
        print('SVN diff')