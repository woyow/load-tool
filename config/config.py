from helpers.distributor import distribute_load
from icecream import ic
from colorama import Fore

#ic.disable() # Disable logs

class Config:

  def __init__(self, cmd_args):
    self.process = self.validate_process(cmd_args.process)
    self.thread = self.validate_thread(cmd_args.thread)
    self.sleep = self.validate_sleep(cmd_args.sleep)
    self.count = self.validate_count(cmd_args.count)

  def validate_process(self, process):
    " Validating process argument "
    try:
      process = abs(int(process))
      if process == 0:
        raise Exception
      return process
    except:
      self._error('--process', 'positive integer')

  def validate_thread(self, thread):
    try:
      thread = abs(int(thread))
      return thread
    except:
      self._error('--thread', 'integer')

  def validate_sleep(self, sleep):
    try:
      sleep = abs(float(sleep))
      return sleep
    except:
      self._error('--sleep', 'integer or floar')

  def validate_count(self, count):
    try:
      count = abs(int(count))
      return count
    except:
      self._error('--count', 'integer')

  def configurate_load(self):
    " Get load balanced arrays for processes and threads "
    proc_load = distribute_load(self.count, self.process)
    ic(proc_load)
    thread_load = [0 for i in range(len(proc_load))]
    for i in range(len(proc_load)):
      thread_load[i] = distribute_load(proc_load[i], self.thread)
    ic(thread_load)

    return proc_load, thread_load

  def configurate_sleep_interval(self):
    " Get a sleep interval "
    return self.sleep

  def _error(self, parameter, type):
    raise Exception (Fore.RED + f'Parameter {parameter} need {type} value' + Fore.RESET)
