#! /usr/bin/env python3

from functools import wraps, partial
from helpers.locker import Locker
import time

l = Locker()

def sleep_interval(func=None, sleep_time=None):
  """
  Sleep decorator for payload

  args:
    - func: Wrapped function
    - sleep_time: Sleep interval between execution payload

  use:
    - without argument: @sleep_interval()
    - with argument: @sleep_interval(sleep_time=1)
  """
  if func is None:
    return partial(sleep_interval, sleep_time=sleep_time)

  @wraps(func)
  def wrapper(*args, **kwargs):
    l.lock_proc()
    l.lock_thread()
    func(*args, **kwargs)
    if sleep_time is not None:
      time.sleep(sleep_time)
    l.unlock_thread()
    l.unlock_proc()
  return wrapper
