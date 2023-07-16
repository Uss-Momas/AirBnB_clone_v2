#!/usr/bin/python3
"""pack web static module"""
from fabric.api import *
from datetime import datetime
from os.path import isdir

env.hosts = ["54.208.202.40", "100.24.255.115"]
env.user = "ubuntu"
env.key_filename = '~/.ssh/id_rsa'


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


def do_deploy(archive_path):
    """Fabric script that distributes an archive to web servers"""
    import os

    try:
        if os.path.exists(archive_path):
            archive_list = archive_path.split('/')
            archive_tgz = archive_list[1]
            archive_name = archive_tgz.split(".")[0]
            put(archive_path, "/tmp")
            web_dir = "/data/web_static/releases/{}".format(archive_name)
            run("sudo mkdir -p {}".format(web_dir))
            tmp_arc_tgz = "/tmp/{}".format(archive_tgz)
            run("sudo tar -xzf {} -C {}".format(tmp_arc_tgz, web_dir))
            run("sudo rm {}".format(tmp_arc_tgz))
            source = web_dir + "/web_static/*"
            destiny = web_dir
            run("sudo mv -n {} {}".format(source, destiny))
            run("sudo rm -rf {}/web_static".format(web_dir))
            current_symb_link = "/data/web_static/current"
            run("sudo rm -rf {}".format(current_symb_link))
            run("sudo ln -s {} {}".format(web_dir, current_symb_link))
            run("sudo service nginx restart")
            return True
        else:
            print("File doesn't exist")
            return False
    except Exception:
        return False


def deploy():
    """Creates and distributes an archive to my web servers"""
    archive_path = do_pack()
    if archive_path:
        print("==================Deploying the files==================")
        do_deploy(archive_path)
    else:
        return False
