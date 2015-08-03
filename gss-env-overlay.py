#!/usr/bin/python

import os
import subprocess
import argparse
import time

# Argument parse for username
parser = argparse.ArgumentParser(description="GSS Environment Overlay.")
parser.add_argument('--user', '-u', action="store", dest="user", help="Username of GSS user")                    
args = parser.parse_args()   

setup_path = '/etc/gss-env-overlay/'
support_dir = '/var/support/gss/'

def get_user():  
    if not args.user:
        user = raw_input("Username: ")
    
    else:
        user = args.user
    
    return check_user(user)

def check_user(user):      
    # Who are the people we have files for?
    gss_users = os.listdir(setup_path+"/home/")
    print gss_users
    
    while user not in gss_users:
        user = raw_input("No environment found.\n\nUsername: ")
    return user 
            
def screenrc_setup(user):
    try:
        rc_file = open("/etc/gss-env-overlay/screenrc" , "w+")
    except IOError, e:
#        if e.errno != 17:
#            raise 
        os.mkdir("/etc/gss-env-overlay", 0755)
        rc_file = open("/etc/gss-env-overlay/screenrc" , "w+")
    
    if not os.path.exists(support_dir):
        os.mkdir(support_dir)

    warning = "WARNING: This file will be over-written on each iteration by the script.\n\n"
    rc_file.write(warning)    

    rc_file.write("logfile /var/support/gss/%s.%s\n" % (user, start_time))
    rc_file.close()

def start_screen(user):
    bashrc_file = "/%s/home/%s/.bashrc" % (setup_path , user)
    bash_setup = "exec /bin/bash -rcfile %s" % bashrc_file

    subprocess.call(['screen', '-dmSL' , user , '-c' , "/etc/gss-env-overlay/screenrc" , 'sh' , '-c' , bash_setup])

start_time = time.time()
user = get_user()
screenrc_setup(user)
start_screen(user)

subprocess.call(["screen" , "-r"])
