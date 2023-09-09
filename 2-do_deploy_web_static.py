#!/usr/bin/python3
""" a Fabric script (based on the file 1-pack_web_static.py) that distributes..
    ..an archive to your web servers, using the function do_deploy: """
from fabric.api import env, put, run
from os.path import exists

# Define the web servers
env.hosts = ['34.229.55.2', '100.26.178.240']

def do_deploy(archive_path):
    if not exists(archive_path):
        return False
    
    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        
        # Extract the archive to the folder /data/web_static/releases/<archive filename without extension>
        filename = archive_path.split('/')[-1]
        folder_name = "/data/web_static/releases/{}".format(filename.split('.')[0])
        run("mkdir -p {}".format(folder_name))
        run("tar -xzf /tmp/{} -C {}".format(filename, folder_name))
        
        # Delete the archive from the web server
        run("rm /tmp/{}".format(filename))
        
        # Move the contents of the extracted folder to the parent directory
        run("mv {}/web_static/* {}/".format(folder_name, folder_name))
        run("rm -rf {}/web_static".format(folder_name))
        
        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")
        
        # Create a new symbolic link /data/web_static/current
        run("ln -s {} /data/web_static/current".format(folder_name))
        
        print("New version deployed!")
        return True
    
    except Exception as e:
        print(str(e))
        return False
