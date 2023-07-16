#!/usr/bin/python3
"""pack web static module"""
from fabric.api import *
from datetime import datetime
from os.path import isdir


def do_pack():
    """generates a .tgz archive from contents of a folder"""
    try:
        if isdir("versions") is False:
            local("mkdir -p versions")
        time = datetime.now()
        date = time.strftime('%Y%m%d%H%M%S')
        file_path = 'versions/web_static_{}.tgz'.format(date)
        local("tar -cvzf {} web_static".format(file_path))
        return file_path
    except Exception:
        return None
