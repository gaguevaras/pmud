#!/usr/bin/env python
import telnetlib
import argparse
from aliases import alias_list, Alias
from triggers import trigger_list, Trigger
from mud import Mud

parser = argparse.ArgumentParser(description='GBLabs MUD client.')
parser.add_argument('host', metavar='H', type=str, nargs='?', default='kotl.org', help='the target hostname (default=kotl.org)')
parser.add_argument('port', metavar='P', type=int, nargs='?', default=2222, help='the target port (default=2222)')

args = parser.parse_args()

HOST = args.host
PORT = args.port

tn = telnetlib.Telnet(HOST, PORT)

mud = Mud(tn)

for alias in alias_list:
    Alias(mud, alias['name'], alias['func'])

for trigger in trigger_list:
    Trigger(mud, trigger['name'], trigger['func'])

mud.mud_interact()

