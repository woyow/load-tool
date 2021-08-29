#! /usr/bin/env python3
"""
THAT'S AN EXAMPLE!!!

Edit payload function

For local debug payload - run: ./payload.py
"""
import time
import socket
import requests

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
requests_session = requests.session()


def payload(*args, **kwargs):
  print("Global counter:", *args)
  first_example()
  second_example()

def first_example():
  ip = '84.201.139.248'
  port = 80
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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

  r = requests_session.get(url, headers = headers, timeout=(1, 1))
  print(r.content)

if __name__ == "__main__":
  counter = 1
  for i in range(2):
    payload(counter)
