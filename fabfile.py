from  fabric.api import *

env.ssh_config_path = '/Users/neeraj/.ssh/config'
env.use_ssh_config = True

def checkdir(dirname):
    run ( "ls -ltrh %s" %dirname )