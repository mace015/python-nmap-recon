#!/usr/bin/python

from shutil import which

import subprocess
import sys
import os

if not os.path.exists('output'):
    os.makedirs('output')

if which("nmap") is None:
    print("nnap not found!");
    exit();

ip = sys.argv[1];
ip = sys.argv[1];

print(f"Scanning {ip}, this might take a while...")

subprocess.call(["nmap", "-sC", "-sV", "-oA", "output/"+ip, ip]);

print("Done scanning!");