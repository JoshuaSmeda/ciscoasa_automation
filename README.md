[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Nclose-ZA/ciscoasa_automation/issues)

<h1> Guide on how to use Cisco_Automation script: </h1>
* This script only supports Cisco ASA devices. <br>
* Specifying multiple cisco devices is supported - you'll need to add the devices to the Add_Cisco_Device function which stores Cisco details within a list. See _-mc_ argument or _--help_ <br>
* If there is a demand for a large number of change control configurations to be made to multiple devices quickly - threading can be included. <br>
* You can test connectivity to Cisco devices by using cisco_test.py before creating a scheduler - crontab guru <br>

1. Install prerequisties: <br>
`sudo pip install -r requirements.txt`

2. View available argument options by running the following: <br>
`python cisco_automation.py --help`

3. Insert necessary change control commands - note that these commands must be run within en / conf term on the Cisco device:<br>
```
vi change_control.conf
```
Include the cisco commands you wish to run - one command per line. Specify file when running the script (see option 2) 

If you wish to specify multiple Cisco devices by running the following (replace the IP's with your actual IP's): <br>
`python cisco_automation.py -mc 192.168.1.1, 192.168.1.2, 192.168.1.3`
