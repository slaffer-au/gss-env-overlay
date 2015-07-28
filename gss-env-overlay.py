#!/usr/bin/python

import os
import subprocess
import argparse

# Who are the people we have files for?
gss_users = ["slaffer" , "gchami"]

# Argument parse for username
parser = argparse.ArgumentParser()
parser.add_argument('--user', '-u', action="store", dest="user", help="Username of GSS user")                    
args = parser.parse_args()   

def check_user(user):
    while user not in gss_users:
        user = input("No environment found for %s.\n\nUsername: ")

if not args.user:
    user = input("Username: ")
    check_user(user)
