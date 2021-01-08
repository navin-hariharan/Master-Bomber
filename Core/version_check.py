import subprocess
import ctypes
from os import system, getuid, path
from time import sleep
import requests
from platform import system as systemos, architecture
from subprocess import check_output
import multiprocessing
import gettext
import sys
import ssl
from os import system, environ

if(not environ.get('PYTHONHTTPSVERIFY', "") and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context
RED, WHITE, CYAN, GREEN, DEFAULT = '\033[91m', '\033[46m', '\033[36m', '\033[1;32m',  '\033[0m'
def verCheck():
    system('clear')
    print("{1}[{0}>{1}] {0}Checking For Updates{2}...".format(GREEN, RED, DEFAULT ))
    ver_url = 'https://raw.githubusercontent.com/navin-hariharan/Master-Bomber/master/Core/version.txt'
    ver_rqst = requests.get(ver_url)
    ver_sc = ver_rqst.status_code
    if ver_sc == 200:
        with open('Core/version.txt') as f:
            ver_current = f.read()
            ver_current = ver_current.strip()
            github_ver = ver_rqst.text
            github_ver = github_ver.strip()
        if ver_current == github_ver:
            print("{1}[{0}+{1}] {0}[Up-To-Date]- {2}v {3}".format(GREEN, RED, DEFAULT, github_ver))
        else:
            print("{1}[{0}>{1}] {0}Their Is A Newer Version Available{2}.\n".format(GREEN, RED, DEFAULT))
            print("{1}[{0}+{1}] {0}[Current]- {2}v {3}\n{1}[{0}+{1}] {0}[Available]- {2}v.{4}".format(GREEN, RED, DEFAULT, ver_current, github_ver)) 
            print("{1}[{0}>{1}] {1}Updating To The Latest Version {0}[v {3}]... \n{1}[{0}>{1}] {0}Please Wait\n".format(GREEN, RED, DEFAULT, github_ver))
            sleep(2)
            system("git clone https://github.com/navin-hariharan/Master-Bomber ../TEMP")
            system("cd ..;rm -rf  Master-Bomber;mv TEMP Master-Bomber;cd Master-Bomber;chmod +x *")
            system("echo 'RESTART THE TERMINAL'")
    else:
        print('{1}[{0}^{1}] {0}Failed To Get Update [Status:{1}{3}{0}]\n'.format(GREEN, RED, DEFAULT))
system("cd ..")
verCheck()
