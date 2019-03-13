import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-f', "--file", help='Import a change control configuration', required=True)
parser.add_argument("-d", "--device_ip", help="Specify Cisco device IP")
parser.add_argument("-u", "--username", help="Specify Cisco username")
parser.add_argument("-p", "--password", help="Specify Cisco password")
parser.add_argument("-mc", "--multiple-ciscos", help="Specify multiple Cisco devices - must be seperated by , ")
args = parser.parse_args()
