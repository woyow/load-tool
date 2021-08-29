#! /usr/bin/env python3

import argparse
import sys
from helpers.runner import Runner

def main():
  r = Runner(cmd_args)
  r()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog='main.py')
  parser.add_argument('-p', '--process', default=1, help='Set processes count. Default - 1')
  parser.add_argument('-t', '--thread', default=0, help='Set threads count. Default - 0')
  parser.add_argument('-s', '--sleep', default=0, help='Set sleep interval. Default - 0 seconds')
  parser.add_argument('-c', '--count', default=1, help='Set count of exec your payload. Default - 1')
  cmd_args = parser.parse_args()
  print(cmd_args)
  sys.exit(main())

