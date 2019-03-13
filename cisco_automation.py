#usr/bin/python
# -*- coding: utf-8 -*-

from netmiko import ConnectHandler
import getpass
from datetime import datetime
import time
from documentation.help import *
import smtplib, ssl

__author__ = 'Joshua Smeda'
__company__ = 'Nclose'
__sourcecode__ = 'https://github.com/ktbyers/netmiko'
__version__ = '0.2.0'
__email__ = 'joshua@nclose.com'
__status__ = 'Prod'

class main:

	def __init__(self, device_type, host, username, password):
		self.device_type = device_type
		self.host = host
		self.username = username
		self.password = password
		self.device_dict = { 'device_type': device_type, 'host': host, 'username': username, 'password': password }
		self.session = ConnectHandler(**self.device_dict)

	def run_command(self, cmd):
		self.session.find_prompt()
		terminal_output = self.session.send_config_set(config_commands)
		self.session.disconnect()
		return terminal_output

def Commands(command):
	for device in cisco_list:
		output = device.run_command(command)
		print("[*] Output from:\n " + device.host)
		print("[*] Configuration changes made:\n " + str(output))
		total_time = datetime.now() - startTime
		print("Total run time: " + str(total_time))
		Send_Email(output, device.host, total_time)

def Send_Email(output, device_IP, total_time):
	subject = str('Truworths Cisco Automation Run: ' + device_IP)
	total_time = str(total_time)
	toaddr = 'firewallops@nclose.com'
	fromaddr = 'nclose.ciscoautomation@gmail.com'
	body = str("Terminal output of change control: " + "\n" + "\n" + output + "\n" + "\n" + "Total Automation run time: " + total_time)
	msg = """From: %s\nTo: %s\nSubject: %s\n\n%s """ % (fromaddr, toaddr, subject, body)
	try:
		mail = smtplib.SMTP('smtp.gmail.com', 587)
		mail.ehlo()
		mail.starttls()
		mail.login('nclose.ciscoautomation@gmail.com', 'b3}Au8VL5`bdbkc7')
		mail.sendmail('nclose.ciscoautomation@gmail.com', 'firewallops@nclose.com', msg)
		mail.close()
		print("Mail Sent successfully!")
	except Exception, e:
		print("Mail Send Error! " + str(e))

def Add_Cisco_Device(device_type, host, username, password):
	cisco_device = main(device_type, host, username, password)
	cisco_list.append(cisco_device)

cisco_list = []

startTime = datetime.now()

if args.device_ip and args.username and args.password:
	print("Arguments provided - attempting to log on device!")
	Add_Cisco_Device('cisco_asa', args.device_ip, args.username, args.password)

elif args.username and args.password and args.multiple_ciscos:
	print("Multiple cisco device argument supplied")
	result = [x.strip() for x in args.multiple_ciscos.split(',')]
	print(result)
        for device in result:
		Add_Cisco_Device('cisco_asa', device , args.username, args.password)
		print(cisco_list)

else:
	print("No arguments provided - requesting access details: ")
	device_type = 'cisco_asa'
	device_IP = raw_input('Device IP: ')
	un = raw_input('Username: ')
	pw = getpass.getpass()
	Add_Cisco_Device(device_type, device_IP, un, pw)

with open(args.file) as f:
	file_content = f.readlines()
	config_commands = [x.strip() for x in file_content]
	Commands(config_commands)
