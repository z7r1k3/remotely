#!/usr/bin/env python
#
#
# remotely
# a remote host manager

from resources import connect, hosts
import argparse

# Parser
parser = argparse.ArgumentParser()

parser.add_argument('-a', '--add',
                    help='add a new host',
                    action='store_true')
parser.add_argument('-e', '--edit',
                    help='edit existing host',
                    action='store_true')
parser.add_argument('-r', '--remove',
                    help='remove a host',
                    action='store_true')
parser.add_argument('-P', '--protocol', help='protocol to connect with')
parser.add_argument('-H', '--host', help='specify a saved hostname')

args = parser.parse_args()

# Args
if args.add and args.host:
    hosts.add(args.host)
elif args.edit and args.host:
    hosts.edit(args.host)
elif args.remove and args.host:
    hosts.remove(args.host)
elif args.host:
    host = hosts.read(args.host)

    if args.protocol == 'sftp':
        connect.sftp(host['ip'],
                     host['port'],
                     host['user'])
    else:  # Default
        connect.ssh(host['ip'],
                    host['port'],
                    host['user'])
else:
    # TODO: handle no_args no_values (select a host from list)
    # i.e. 'python remotely.py'
    # TODO: handle no_args with one value (connect to host via default proto)
    # i.e. 'python remotely.py <hostname>'
    print('No args')

# Default to displaying host-list
