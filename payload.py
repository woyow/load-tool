#! /usr/bin/env python3
"""
THAT'S AN EXAMPLE!!!

Edit payload function

For local debug payload - run: ./payload.py
"""

import socket
import requests

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
requests_session = requests.session()


def payload(*args, **kwargs):
  print("Global counter:", *args)
  first_example()
  second_example()

def first_example():
  ip = '142.251.1.101'
  port = 80
  s.connect((ip, port))
  s.sendto(("GET /" + ip + " HTTP/1.1\r\n").encode('ascii'), (ip, port))
  print("OK!")
  s.close()

def second_example():
  url = "https://google.com"
  headers = {'User-Agent': 'load-tool',
  'Content-Type': 'application/json',
  'Connection':'close'
  }
  data = {'"test":"test"'}
  r = requests_session.get(url, headers = headers, timeout=(1, 1))
  print(r.content)

if __name__ == "__main__":
  counter = 1
  payload(counter)
