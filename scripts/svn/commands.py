import os
import re
import subprocess

from scripts.general.cmd import *
from scripts.general.explorer import *

VALID_ACCEPT_FLAGS = [
    'p','e','l','mf','tf','mc','tc','tf'
]

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
    """
    SVN commands object
    """

    @staticmethod
    def update(path, rev=None, accept='p'):
        """
        Update working copy.
        
        http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.update.html
        """
        cmd = 'svn update --force '
        if accept not in VALID_ACCEPT_FLAGS:
            cmd += '--accept p ' #So script doesn't stall
        else:
            cmd += '--accept {} '.format(accept)

        if _is_valid_revision(rev):
            cmd += '-r {} '.format(_format_revision(rev))
        try:
            cmd += '"{}"'.format(is_valid_path(path))
        except InvalidPathException as e:
            #print(e) #Log this somehow
            return False #TODO better error handling

        execute(cmd)
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
        cmd += '"{}"'.format(format_path(path, True))

        execute(cmd)
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

        cmd += '"{}"'.format(format_path(path))

        execute(cmd)
        #TODO Error handling to return 'False' under correct circumstances
        #TODO Implement robust revert in case of the 'cannot rever without reverting children bullshit'

        return True

    @staticmethod
    def cleanup(path, remove_unversioned=True):
        """
        Recursively clean up working copy
        
        http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.cleanup.html
        """
        cmd = 'svn cleanup '

        if remove_unversioned:
            cmd += '--remove-unversioned --remove-ignored '

        cmd += '"{}"'.format(format_path(path))

        execute(cmd)
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