import os
import subprocess

BASE_DIRECTORY = ''

class InvalidPathException(Exception):
    pass


def _execute(cmd):
    p = subprocess.Popen(cmd, shell=True, \
            stdout=subprocess.PIPE, \
            stderr=subprocess.STDOUT)
    output, stderr = p.communicate()

    return output, stderr
    
def _is_valid_path(path):
    """
    Verify the path either exists or can be created.
    
    :param path: relative path
    """
    path = _format_path(path)

    if os.isdir(path):
        return path
    try:
        os.makedirs(path, exist_ok=True)
    except OSError:
        raise InvalidPathException('Invalid path: ' + path) # Invalid path
    
    return path

def _format_path(path):
    # Let's assume people will provide valid paths
    path = path.lstrip('/\\')
    path = path.rstrip('/\\')

    return BASE_DIRECTORY + path

def _is_valid_revision(rev):
    """Verify the revision parameter"""

    #TODO: revisions can be a range - probably not too useful atm
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
        """
        Update working copy.
        
        http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.update.html
        """
        cmd = 'svn update --force '
        if _is_valid_revision(rev):
            cmd += '-r {} '.format(_format_revision(rev))
        cmd += '"{}"'.format(_format_path(path))

        print(cmd)
        _execute(cmd)

    @staticmethod
    def checkout(path, rev=None):
        """
        Checkout working copy from repo.
        
        http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.checkout.html
        """
        cmd = 'svn checkout --force '
        if _is_valid_revision(rev):
            cmd += '-r {} '.format(_format_revision(rev))
        cmd += '"{}"'.format(_format_path(path))

        print(cmd)
        _execute(cmd)

    @staticmethod
    def revert():
        """
        Revert any local modifications
        
        http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.revert.html
        """
        print('SVN Revert')

    @staticmethod
    def cleanup():
        """
        Recursively clean up working copy
        
        http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.cleanup.html
        """
        print('SVN Cleanup')

    @staticmethod
    def merge():
        """
        Merge changes from working path to destination.
        
        http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.merge.html
        """
        print('SVN Merge')

    @staticmethod
    def delete():
        """
        Remove file from working copy.
        
        http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.delete.html
        """
        print('SVN delete')

    @staticmethod
    def add():
        """
        Add to the repository.
        
        http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.add.html
        """
        print('SVN add')

    @staticmethod
    def log():
        """
        Display commit log messages.
        
        http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.log.html
        """
        print('SVN log')

    @staticmethod
    def commit():
        """
        Commit changes to repo.
        
        http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.commit.html
        """
        print('SVN commit')

    @staticmethod
    def unlock():
        """
        Unlock working copy path URLs
        
        http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.unlock.html
        """
        print('SVN unlock')

    @staticmethod
    def info():
        """
        Display useful information about a local/remote items
        
        http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.info.html
        """
        print('SVN info')

    @staticmethod
    def diff():
        """
        Display difference between two revisions
        
        http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.diff.html
        """
        print('SVN diff')

    @staticmethod
    def mkdir():
        """
        Create new directory in working copy
        
        http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.mkdir.html
        """
        print('SVN mkdir')

    @staticmethod
    def patch():
        """
        Apply patch to directory
        
        http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.patch.html
        """
        print('SVN patch')

    @staticmethod
    def proplist():
        """
        List all properties
        
        http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.proplist.html
        """
        print('SVN proplist')

    @staticmethod
    def propdelete():
        """
        Remove property from item.
        
        http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.propdel.html
        """
        print('SVN propdelete')