#!/usr/bin/python3
"""pack web static module"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """generates a .tgz archive from contents of a folder"""
    try:
        local("mkdir -p versions")
        time = datetime.now()
        date = time.strftime('%Y%m%d%H%M%S')
        file_path = 'versions/web_static_{}.tgz'.format(date)
        local("tar -cvzf {} ./web_static".format(file_path))
        return file_path
    except Exception:
        return None
