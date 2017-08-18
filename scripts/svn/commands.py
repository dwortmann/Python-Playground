import os
import subprocess

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
    path = _format_path(path)

    if os.path.isdir(path):
        return path
    elif not create_if_needed:
        raise InvalidPathException('Path does not exist: ' + path)

    try:
        print('there')
        os.makedirs(path, exist_ok=True)
    except OSError:
        raise InvalidPathException('Invalid path: ' + path) # Invalid path

    return path

def _format_path(path):
    # Let's assume people will provide valid paths
    path = path.lstrip('/\\')
    path = path.rstrip('/\\')

    return path

def _is_valid_revision(rev):
    """Verify the revision parameter"""

    #TODO: revisions can be a range - probably not too useful atm
    if not rev:
        return False
    if isinstance(rev, int) and rev > 0:
        return True
    if isinstance(rev, str) and rev.isdigit():
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
        cmd = 'svn update --force --accept tc '
        if _is_valid_revision(rev):
            cmd += '-r {} '.format(_format_revision(rev))
        try:
            cmd += '"{}"'.format(_is_valid_path(path))
        except InvalidPathException as e:
            #print(e) #Log this somehow
            return False #TODO better error handling

        print(cmd)
        _execute(cmd)
        #TODO Error handling to return 'False' under correct circumstances

        return True

    @staticmethod
    def checkout(path, rev=None):
        """
        Checkout working copy from repo.
        
        http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.checkout.html
        """
        cmd = 'svn checkout --force '
        if _is_valid_revision(rev):
            cmd += '-r {} '.format(_format_revision(rev))
        cmd += '"{}"'.format(_format_path(path, True))

        print(cmd)
        _execute(cmd)
        #TODO Error handling to return 'False' under correct circumstances

        return True

    @staticmethod
    def revert(path, depth='infinity', recursive=True):
        """
        Revert any local modifications
        
        http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.revert.html
        """
        cmd = 'svn revert '

        if recursive:
            cmd += '--recursive '

        if depth == 'infinity':
            cmd += '--depth={} '.format(depth)
        else:
            print('depth parameter not supported yet')

        cmd += '"{}"'.format(_format_path(path))

        print(cmd)
        _execute(cmd)
        #TODO Error handling to return 'False' under correct circumstances
        #TODO Implement robust revert in case of the 'cannot rever without reverting children bullshit'

        return True

    @staticmethod
    def cleanup(path):
        """
        Recursively clean up working copy
        
        http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.cleanup.html
        """
        cmd = 'svn cleanup '
        cmd += '"{}"'.format(_format_path(path))
        
        print(cmd)
        _execute(cmd)
        #TODO Error handling to return 'False' under correct circumstances

        return True

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