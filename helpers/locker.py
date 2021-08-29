from multiprocessing import Lock as plock
from threading import Lock as tlock
from functools import wraps

class Locker(object):

  def __init__(self):
    self.plock = plock()
    self.tlock = tlock()

  def lock_proc(self):
    " Lock execution in others process "
    return self.plock.acquire()

  def unlock_proc(self):
    " Unlock execution in others process "
    return self.plock.release()

  def lock_thread(self):
    " Lock execution in others thread on current process "
    return self.tlock.acquire()

  def unlock_thread(self):
    " Unlock execution in others thread on current process "
    return self.tlock.release()
