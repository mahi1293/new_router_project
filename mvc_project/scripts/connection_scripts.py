import telnetlib

HOST = '127.0.0.1'
PORT = 8090
# from pudb import set_trace; set_trace()
tn = telnetlib.Telnet(HOST, PORT)
tn.set_debuglevel(100)
data = tn.read_all(timeout=1)
print("Data: " + data)

tn.close()


import subprocess
import sys


HOST = "mahena@192.168.31.122"
COMMAND = "ls"

ssh_obj = subprocess.Popen(
            ["ssh", "%s" % HOST, COMMAND],
            shell=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

result = ssh_obj.stdout.readlines()
if result == []:
    err = ssh_obj.stderr.readlines()
    print(sys.stderr, "ERROR: %s" % err)
else:
    print(result)



import pysftp
import os

SFTP_HOST = "192.168.31.122"
SFTP_USER = "Mahena"  # noqa:W605
SFTP_PASSWORD = "Apr@2020"
SFTP_PACKAGE_FOLDER = "/home/mahena/Downloads"

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

with pysftp.Connection(SFTP_HOST, username=SFTP_USER, password=SFTP_PASSWORD, private_key=".ppk", cnopts=cnopts) as sftp:
    dir = SFTP_PACKAGE_FOLDER
    print("dir------", dir)
