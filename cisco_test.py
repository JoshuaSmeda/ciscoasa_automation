#usr/bin/python
# -*- coding: utf-8 -*-

from netmiko import ConnectHandler
import getpass
import click
from datetime import datetime
import time
import logging

__author__ = 'Joshua Smeda'
__company__ = 'Nclose'
__sourcecode__ = 'https://github.com/ktbyers/netmiko'
__version__ = '0.2.0'
__email__ = 'joshua@nclose.com'
__status__ = 'Dev'


logging.basicConfig(filename='debug.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

def main():
	if click.confirm('[*] Test Connectivity To Cisco Device. DOES NOT EXECUTE CODE!', default=False):
		print('Please input the following details: ')
		ip = raw_input('Device IP: ')
		un = raw_input('Username: ')
		pw = getpass.getpass()
		cisco_asa = {
			'device_type': 'cisco_asa',
			'ip': ip,
			'username': un,
			'password': pw,
			#Disable secret to enter priv mode on ASA
			'secret': pw,
			'verbose': False,
		}
		try:
			net_connect = ConnectHandler(**cisco_asa)
			net_connect.enable(cmd="login")
			prompt = net_connect.find_prompt()
			net_connect.disconnect()
			print(prompt)
			print("Appears to be working correctly!")
		except Exception, e:
			print("Error when connecting: " + str(e))

if __name__ == "__main__":
	main()
