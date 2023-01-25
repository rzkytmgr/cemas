"""
  ______ __ __  __    __  
 / _/ __|  V  |/  \ /' _/ 
| \_| _|| \_/ | /\ |`._`. v1.0.0
 \__/___|_| |_|_||_||___/ Content Manage System Mass Scanner
"""

import os
import argparse
from time import sleep
from util import Logger
from lib.core import Core
from threading import Thread
from datetime import datetime
from termcolor import colored
from urllib3 import PoolManager
from constant import AVAILABLE_SCANNER
from lib import arg_file_validator, arg_cms_validator

log = Logger()

def main():
  log.custom(text="  ______ __ __  __    __  ", color='light_cyan', attrs=['bold'])
  log.custom(text=" / _/ __|  V  |/  \ /' _/ ", color='light_cyan', attrs=['bold'])
  log.custom(text="| \_| _|| \_/ | /\ |`._`. v1.0.0", color='light_cyan', attrs=['bold'])
  log.custom(text=" \__/___|_| |_|_||_||___/ Content Manage System Mass Scanner\n", color='light_cyan', attrs=['bold'])

  parser = argparse.ArgumentParser(usage='%(prog)s -t hostlist.txt [OPTIONAL]', description='a content manage system mass scanner, it will separate the hosts from the list that you have into several parts according to the cms used')
  parser.add_argument('-t', '--target', dest='target', metavar='', help='specify your target files with your hosts lists', type=arg_file_validator, required=True)
  parser.add_argument('-c', '--cms', dest='cms', metavar='', help='specify your target cms default: (include all cms provided by tools)', type=arg_cms_validator, required=False)
  parser.add_argument('-d', '--out-dir', dest='dir', metavar='', help='specify the output directory', required=False)
  parser.add_argument('--timeout', dest='timeout', metavar='', type=int, help='specify maximum timeout when give requesting to a host', required=False, default=5)
  parser.add_argument('--thread', dest='thread', metavar='', type=int, help='specify max thread that you want', required=False, default=5)
  args = parser.parse_args()

  log.unique(f'Starting {colored("Cemas Scanner v1.0.0", color="light_cyan")}')
  log.tab('Fast Content Management System Mass Scanner')
  log.tab(f'find more information here: {colored("https://github.com/rzkytmgr/cemas", color="light_cyan")}')

  args.target = os.path.join(os.path.dirname(__file__), args.target)
  log.info(f'Target file path {colored(args.target, color="light_yellow")}')


  if args.cms is None:
    args.cms = AVAILABLE_SCANNER
  
  
  if args.dir is None:
    for i in range(0, 9999):
      args.dir = os.path.join(os.path.dirname(__file__), 'output', f'{datetime.now().strftime("%Y-%m-%d")}-{i}')
      if not os.path.exists(args.dir):
        break
  else:
    args.dir = os.path.join(os.path.dirname(__file__), 'output', args.dir)
  log.info(f'Output directory {colored(args.dir, color="light_yellow")}')
  log.success(f'Setup successfully, Scan starting')

  sleep(1)
  
  start = 0
  end = int(args.thread)
  core = Core(args.dir, int(args.timeout))

  with open(args.target, 'r') as file:
    targets = file.readlines()
    scanned = 0
    while start < len(targets):
      threads = list()
      for target in targets[start:end]:
        scanned += 1
        log.info(f'Processing ({colored(scanned, color="light_yellow")}/{colored(len(targets), color="light_yellow")})', end='\r')
        thread = Thread(target=core.scan, args=(target.strip(), args.cms))
        threads.append(thread)
        thread.start()

      for thread in threads:
        thread.join()
      
      start = end
      end += args.thread

if __name__ == "__main__":
  main()
