#!/usr/bin/python

import os
import subprocess
import argparse


# Argument parse for username
parser = argparse.ArgumentParser(description="GSS Environment Overlay.")
parser.add_argument('--user', '-u', action="store", dest="user", help="Username of GSS user")                    
args = parser.parse_args()   

def get_user():
    
    # Who are the people we have files for?
    gss_users = ["slaffer" , "gchami"]    

    def check_user(user):
        while user not in gss_users:
            user = raw_input("No environment found.\n\nUsername: ")
        return user

    if not args.user:
        user = raw_input("Username: ")
    
    else:
        user = args.user
    
    return check_user(user)


user = get_user()
bashrc_file = "/tmp/%s.bashrc" % user

bash_setup = "exec /bin/bash -rcfile %s" % bashrc_file

print bashrc_file
print bash_setup

subprocess.call(['screen', '-dmS' , user ])