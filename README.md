# lld-processes
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/bloodia/Zabbix-Low-Level-Discovery/blob/master/lld-processes/LICENSE.md)
[![Build Status](https://travis-ci.org/bloodia/Zabbix-Low-Level-Discovery.svg?branch=master)](https://travis-ci.org/bloodia/Zabbix-Low-Level-Discovery)

## Overview
Zabbix customized server-side scripts for processes low level discovery.

## Requires
### OS
- CentOS 5.x - 7.x

### Python
- 2.6
- 2.7
- 3.2
- 3.3
- 3.4
- 3.5

### Python Modules
- json
- subprocess
- re
- argparse

## Script Usage
```
usage: lld-processes.py [-h] [-v] [-u PSUSER] [-n PSNAME]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show version and exit
  -u PSUSER, --psuser PSUSER
                        select process user
  -n PSNAME, --psname PSNAME
                        select process name

for example: /usr/local/bin/lld-processes.py -t 'zabbix' -n '/usr/sbin/zabbix_server'
```

## Install Script
Create directory "/usr/local/bin" and copy "Custom Script" file (py) to inside.  
Change "Custom Script" file (py) to 555 or dr-xr-xr-x using chmod.  

## Install UserParameter Config
Copy "UserParameter Config" file (conf) to /etc/zabbix/zabbix_agentd.d and restart Zabbix agent.  

## Author
[@bloodia](https://twitter.com/bloodiadotnet)
