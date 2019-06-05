[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Nclose-ZA/ciscoasa_automation/issues)

<h1>Guide on how to use Cisco_Automation script: </h1> <br>
* Note: This script only supports Cisco ASA. <br>
* Multiple Cisco devices is supported - you'll need to add the devices to the Add_Cisco_Device function which stores Cisco details within a list. <br>
* If there is a demand for a large number of change control configurations to be made to multiple devices - threading can be included into the main() class. <br>
* To add slack_intergration or mail notification <br>
* You can test connectivity to Cisco devices by using cisco_test.py before creating a scheduler - crontab guru <br>


1. Install prerequisties: <br>
`sudo pip install -r requirements.txt`


2. View available argument options by running the following: <br>
`python cisco_automation.py --help`


3. Create a change control file and insert necessary change control commands - note that these commands must be run within en / conf term.<br>
```

Touch change_control.txt 
# Include the cisco commands you wish to run - one command per line. (\n)
Specify file when running the script (see option 2) 

```

4. Specify multiple Cisco devices by running the following(replace the IP's with your actual IP's): <br>
`python cisco_automation.py -mc 192.168.1.1, 192.168.1.2, 192.168.1.3`
