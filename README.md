[*] Guide on how to use Cisco_Automation script: <br>
[*] Note: This script only supports Cisco ASA. <br>
[*] Multiple Cisco devices is supported - you'll need to add the devices to the Add_Cisco_Device function which stores Cisco details within a list. <br>
[*] If there is a demand for a large number of change control configurations to be made to multiple devices - threading can be included into the main() class. <br>
[*] To add slack_intergration or mail notification <br>
[*] You can test connectivity to Cisco devices by using cisco_test.py before creating a scheduler - crontab guru <br>


1. Install prerequisties: <br>
[*] sudo pip install -r requirements.txt


2. View available argument options by running the following: <br>
[*] python cisco_automation.py --help


3. Create a change control file and insert necessary change control commands - note that these commands must be run within en / conf term.<br>
[*] Touch change_control.txt <br>
[*] Import Cisco Commands <br>
[*] Specify file when running the script (see option 2) <br>
