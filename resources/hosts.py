#!/usr/bin/env python3

from datetime import datetime
from os.path import exists
import json


# Primary modules
def add(hostname,
        new_ip=None,
        new_user=None,
        new_port=None):
    # TODO:
    # 1: Do not let user overwrite entries in add mode
    # 2: If command line flags passed new_host values,
    #   do not request them on first loop only
    # 3: Need to be able to create new hosts.json,
    #   currently errors if it doesn't exist
    confirmed = False
    cancelled = False

    while not confirmed:
        new_ip = input('What is the IP of the host?\n')
        new_user = input('\nWhat is the username for the host?\n')
        new_port = input('\nWhat is the port for the host?\n')

        confirm_input = input('\nDoes the following look correct?' +
                              '\nHostname: ' + hostname +
                              '\nIP: ' + new_ip +
                              '\nUser: ' + new_user +
                              '\nPort: ' + new_port +
                              '\n(Y)es, (N)o, (C)ancel\n')

        if confirm_input.lower().startswith('c'):
            cancelled = True

            print('\nCancelling...')

            break

        confirmed = confirm_input.lower().startswith('y')

    if not cancelled:
        new_host = {'ip': new_ip,
                    'user': new_user,
                    'port': new_port}

        if exists('data/hosts.json'):
            append(hostname, new_host)
        else:
            create(hostname, new_host)

        print('\nSuccess')


def edit(hostname):  # TODO: Make this an interactive editor
    add(hostname)


def read(hostname=None):
    try:
        with open('data/hosts.json', 'r') as hosts_file:
            if hostname is not None:
                return json.load(hosts_file)[hostname]
            else:
                return json.load(hosts_file)
    except:
        print('***ERROR: unable to locate \"' + hostname + '\"')


def remove(hostname):  # TODO: Little bit hacky, should improve
    try:
        with open('data/hosts.json', 'r') as hosts_read:
            hosts_data = json.load(hosts_read)

            del hosts_data[hostname]

            with open('data/hosts.json', 'w+') as hosts_write:
                json.dump(hosts_data, hosts_write, indent=4)
    except:
        print('***ERROR: Unable to delete host')


# Secondary modules
def append(hostname, new_host):
    with open('data/hosts.json', 'r+') as hosts_file:
        try:
            hosts_data = json.load(hosts_file)

            hosts_data[hostname] = new_host

            hosts_file.seek(0)

            json.dump(hosts_data, hosts_file, indent=4)
        except:
            if input('***ERROR: hosts.json is unreadable' +
                     '\nWould you like to overwrite it?' +
                     '\n(Y)es, (N)o\n').lower().startswith('y'):

                with (open('data/' +
                           datetime.now().strftime('%Y-%m-%d-%H-%M-%S') +
                           '.hosts.json.bak', 'w+') as hosts_bak,
                      open('data/hosts.json', 'r') as hosts_file):
                    hosts_bak.write(hosts_file.read())

                    create(hostname, new_host)


def create(hostname, new_host):
    with open('data/hosts.json', 'w+') as hosts_file:
        hosts_data = {hostname: new_host}

        json.dump(hosts_data, hosts_file, indent=4)
