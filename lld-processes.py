#!/usr/bin/python
# coding: utf-8
# ==============================================================================
# Script Name     : lld-processes.py
# Tool Version    : 1.0.0
# Arguments       : -
# Options         : -v, --version  print version information.
#                 : -h, --help     show this help message and exit.
#                 : -u, --psuser   select process user
#                 : -n, --psname   select process name
# Usage           : $0 [<Options>]
# OS Version      : CentOS release 5, 6, 7
# ==============================================================================
# Date          Author        Changes
# 2018/04/10    Yuta Akama    New Creation
# ==============================================================================
# --+----1----+----2----+----3----+----4----+----5----+----6----+----7----+----8

import json
import subprocess
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
                       '-v', '--version',
                       action='version',
                       version='1.0.0',
                       help='print version information.'
                   )
parser.add_argument(
                       '-u', '--psuser',
                       action='store',
                       help='select process user'
                   )
parser.add_argument(
                       '-n', '--psname',
                       action='store',
                       help='select process name'
                   )
args = parser.parse_args()

if __name__ == "__main__":
    p1 = subprocess.Popen(['ps', '-ef'], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['awk', '{for(i=8;i<NF;i++){ printf("%s%s",$i,OFS=" ")} print $NF "," $1}'],stdin=p1.stdout,stdout=subprocess.PIPE)
    # skippable set
    p3 = subprocess.Popen(['grep', '-v', '-E', '^grep |^awk |^sed '], stdin=p2.stdout, stdout=subprocess.PIPE)
    stdout, stderr = p3.communicate()
    data = list()
    for line in stdout.split(b'\n'):
        if line:
            ps = line.split(b',')
            psname = ps[0].decode('utf-8')
            psuser = ps[1].decode('utf-8')
            if args.psuser:
                if psuser == args.psuser:
                    if args.psname:
                        m = re.match(r"(%s)" % args.psname, psname)
                        if m:
                            data.append({"{#PSNAME}": psname, "{#PSUSER}": psuser})
                    else:
                        data.append({"{#PSNAME}": psname, "{#PSUSER}": psuser})
            else:
                data.append({"{#PSNAME}": psname, "{#PSUSER}": psuser})
    print(json.dumps({"data": data}, indent=4))
