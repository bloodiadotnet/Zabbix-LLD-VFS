# Zabbix-LLD-VFS
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/bloodiadotnet/Zabbix-LLD-VFS/blob/master/LICENSE)

## Overview
Zabbix customized server-side scripts for virtual file system low level discovery.

## Requires
### OS
- CentOS 5.x - 7.x

### Python
- 2.6
- 2.7
- 3.3
- 3.4
- 3.5
- 3.6

### Python Modules
- json
- re
- argparse

## Script Usage
```
usage: lld-vfs.py [-h] [-v] [-t FSTYPE] [-n FSNAME]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show version and exit
  -t FSTYPE, --fstype FSTYPE
                        select virtual file system type
  -n FSNAME, --fsname FSNAME
                        select virtual file system name

for example: /usr/local/bin/lld-vfs.py -t 'nfs' -n '/data'
```

## How to Install
### Custom Script
- Create directory "/usr/local/bin" and copy "Custom Script" file (py) to inside.  
- Change "Custom Script" file (py) to 555 or dr-xr-xr-x using chmod.  

### UserParameter Config
- Copy "UserParameter Config" file (conf) to /etc/zabbix/zabbix_agentd.d and restart Zabbix agent.  

## Author
[@bloodiadotnet](https://twitter.com/bloodiadotnet)
