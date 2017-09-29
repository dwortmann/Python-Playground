import os

class InvalidPathException(Exception):
    pass

def is_valid_path(path, create_if_needed=False):
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
        os.makedirs(path, exist_ok=True)
    except OSError:
        raise InvalidPathException('Invalid path: ' + path) # Invalid path

    return path

def _format_path(path):
    # Let's assume people will provide valid paths
    path = path.lstrip('/\\')
    path = path.rstrip('/\\')

    return path

def find_file(file, path):
    # Search recursively for file
    file_path = _find_file_recursive(file, path)

    return file_path

def _find_file_recursive(file, path):
    file_path = None
    dir_contents = os.listdir(path)

    # Check if solution in this directory
    try:
        idx = dir_contents.index(file)
        return '{}\{}'.format(path, dir_contents[idx])
    except ValueError:
        #Not in this directory
        pass

    # Check any subdirectories
    for d in dir_contents:
        if not os.path.isdir('{}\{}'.format(path, d)):
            continue

        file_path = _find_file_recursive(file, '{}\{}'.format(path, d))
        if file_path:
            return file_path

    return file_path

#def _delete_non_versioned_files(path, recursive=True):
#    """
#    Delete unversioned files in a directory tree.
#    
#    Absolete as of svn 1.9.5 where svn cleanup has a command for this
#    """
#    POWERSHELL = "svn status --no-ignore | Select-String '^[?I]' | ForEach-Object { [Regex]::Match($_.Line, '^[^\s]*\s+(.*)$').Groups[1].Value } | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue"
#
#    # Write file to directory
#    file_name = '{}\cleanup_bot.ps1'.format(path)
#    if os.path.exists(file_name):
#        os.remove(file_name)
#
#    f = open(file_name, 'w')
#    f.write(POWERSHELL)
#    f.close()
#
#    # Run from powershell
#    command = 'cd "{}" && powershell cleanup_bot.ps1'.format(path)
#    execute(command)