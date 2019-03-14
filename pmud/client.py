#!/usr/bin/env python
import telnetlib
import argparse

parser = argparse.ArgumentParser(description='GBLabs MUD client.')
from aliases import alias_list, Alias
from mud import Mud

HOST = 'kotl.org'
PORT = '2222'

tn = telnetlib.Telnet(HOST, PORT)

mud = Mud(tn)

for alias in alias_list:
    Alias(mud, alias['name'], alias['func'])

mud.mud_interact()

