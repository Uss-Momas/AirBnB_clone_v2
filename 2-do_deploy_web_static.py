#!/usr/bin/python3
"""pack web static module"""
from fabric.api import *
from datetime import datetime
from fabric.network import ssh
ssh.util.log_to_file("paramiko.log", 10)

env.hosts = ["100.26.215.161", "100.24.255.115"]
env.user = "ubuntu"
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Fabric script that distributes an archive to web servers"""
    import os
    try:
        if os.path.exists(archive_path):
            archive_list = archive_path.split('/')
            archive_tgz = archive_list[1]
            archive_name = archive_tgz.split(".")[0]
            print(archive_path)
            print(archive_name)
            put(archive_path, "/tmp")
            web_dir = "/data/web_static/releases/{}".format(archive_name)
            run("sudo mkdir -p {}".format(web_dir))
            tmp_arc_tgz = "/tmp/{}".format(archive_tgz)
            print(tmp_arc_tgz)
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
