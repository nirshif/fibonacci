
#!usr/bin/env python3.8

import subprocess
import os
from argparse import ArgumentParser

parser = ArgumentParser(description='kill process of given port')
parser.add_argument('port', type=int, help='the port you search')

port = parser.parse_args().port

try:
    result = subprocess.run(
        ['lsof', '-n', "-i4TCP:%s" % port],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
except subprocess.CalledProcessError:
    print(f"no processes listening on port {port}")

else:
    listening = None

    for line in result.stdout.splitlines():
        if "LISTEN" in str(line):
            listening=line
            break

    if listening:
        pid = int(listening.split()[1])
        os.kill(pid, 9)
        print(f"kill process {pid}")
    else:
        print(f"no process listen on port {port}")

