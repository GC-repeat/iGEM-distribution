import tempfile
import os
from shutil import copy

from scripts.scriptutils import EXPORT_DIRECTORY


def copy_to_tmp(package=None, exports=None) -> str:
    """Copy test files into a temporary package directory

    :param package: files to go into the package directory
    :param exports: files to go into the exports subdirectory
    :return: temporary package directory
    """
    # make a temporary package directory and export directory
    if exports is None:
        exports = []
    if package is None:
        package = []
    tmp_dir = tempfile.mkdtemp()
    tmp_sub = os.path.join(tmp_dir, 'test_package')
    tmp_export = os.path.join(tmp_sub, EXPORT_DIRECTORY)
    os.mkdir(tmp_sub)
    os.mkdir(tmp_export)
    # copy all of the relevant files
    test_dir = os.path.dirname(os.path.realpath(__file__))
    for f in package:
        copy(os.path.join(test_dir, 'test_files', f), tmp_sub)
    for f in exports:
        copy(os.path.join(test_dir, 'test_files', EXPORT_DIRECTORY, f), tmp_export)
    return tmp_sub