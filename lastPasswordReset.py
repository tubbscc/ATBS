#! python3

import subprocess

def run_command(command):
    p=subprocess.Popen(command,
                       stdout = subprocess.PIPE,
                       stderr = subprocess.STDOUT)
    return iter(p.stdout.readline, b'')
'''
command = 'net user Casey'
for line in run_command(command):
    print(line)
    #print(line)
#print(command)
'''

pw = b'Password expires'             #b is setting to bytes, was getting error about comparing bytes with string
command = 'net user Casey'
for line in run_command(command):
    if pw in line:         #
        print(line)
    #print(line)
#print(command)
