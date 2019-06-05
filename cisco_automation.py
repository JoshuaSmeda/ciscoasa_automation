#!/usr/bin/python
from netmiko import ConnectHandler
import getpass
from datetime import datetime
import time
from documentation.help import *
import smtplib, ssl
import os

class main:
  """
  Instantiating class object and setting up variables to be used during runtime
  """
  def __init__(self, device_type, host, username, password):
    self.device_type = device_type
    self.host = host
    self.username = username
    self.password = password
    self.device_dict = { 'device_type': device_type, 'host': host, 'username': username, 'password': password }
    self.session = ConnectHandler(**self.device_dict)


  """
  Connect to Cisco device and runs the command set. Returns the terminal output for logging later
  """
  def run_command(self, cmd):
    self.session.find_prompt()
    terminal_output = self.session.send_config_set(config_commands)
    self.session.disconnect()
    return terminal_output


"""
Enrich the data we receive back to make it easy to identify which device we're working on (helpful for environments which have a large number of Cisco devices.
"""
def Commands(command):
  for device in cisco_list:
    output = device.run_command(command)
    print("[*] Output from:\n " + device.host)
    print("[*] Configuration changes made:\n " + str(output))
    total_time = datetime.now() - startTime
    print("Total run time: " + str(total_time))
    Send_Email(output, device.host, total_time)
    Dump_File(output)


def Dump_File(output):
  """
  Dumps the output data to a file as well
  """
  now = datetime.now()
  log_date = now.strftime("%Y-%m-%d")
  log_file = str(log_date + "-cisco_output.txt")
  try:
    os.mknod(log_file)
    with open(log_file, 'wa') as f:
      f.write(output)
      f.write("\n")
      f.close()
  except OSError as err:
    with open(log_file, 'wa') as f:
      f.write(output)
      f.write("\n")
      f.close()


def Send_Email(output, device_IP, total_time):
  """
  Setup mail connection using Gmail to send the report via email
  """
  subject = str('BlaBla Cisco Automation Run: ' + device_IP)
  total_time = str(total_time)
  toaddr = 'rcpt@random.com'
  fromaddr = 'sndr@random.com'
  body = str("Terminal output of change control: " + "\n" + "\n" + output + "\n" + "\n" + "Total Automation run time: " + total_time)
  msg = """From: %s\nTo: %s\nSubject: %s\n\n%s """ % (fromaddr, toaddr, subject, body)
  try:
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('sndr@random.com', 'super_strong_password!')
    mail.sendmail('sndr@random.com', 'rcpt@random.com', msg)
    mail.close()
  except Exception as err:
    print("Mail Send Error! " + str(err))


def Add_Cisco_Device(device_type, host, username, password):
  """
  Adds the cisco device to a list so it's easier to manage
  """
  cisco_device = main(device_type, host, username, password)
  cisco_list.append(cisco_device)

cisco_list = []

#Used to count run time per device
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

else:
  print("No arguments provided - requesting access details: ")
  device_type = 'cisco_asa'
  device_IP = raw_input('Device IP: ')
  un = raw_input('Username: ')
  pw = getpass.getpass()
  Add_Cisco_Device(device_type, device_IP, un, pw)


#Reads the config file and grabs each command seperated by a '\n'
with open(args.file) as f:
  file_content = f.readlines()
  config_commands = [x.strip() for x in file_content]
  Commands(config_commands)
