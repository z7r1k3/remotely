#!/usr/bin/env python3

import os


def ssh(ip, port, user):
    os.system('TERM=xterm-256color ssh -p '
              + str(port) + ' ' + str(user) + '@' + str(ip))
    # Get the current OS using os.name.
    # If 'posix', set TERM. If 'nt' (Win), don't


def sftp(ip, port, user):
    os.system('sftp -P ' + str(port) + ' ' + str(user) + '@' + str(ip))


# def scp_action(ip, port, user):
#    os.system('scp -P ' + str(port) + ' ' + str(user) + '@' + str(ip))
