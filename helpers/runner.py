from config.config import Config
from helpers.counter import Counter
from helpers.sleeper import sleep_interval
from payload import payload as user_payload

from multiprocessing import Process, Value
from threading import Thread


class Runner(object):

  def __init__(self, cmd_args):
    self.processes, self.threads = Config(cmd_args).configurate_load()
    self.sleep_time = Config(cmd_args).configurate_sleep_interval()
    self.counter = Value('i', 0) # Global var for multiprocessing

  def __call__(self):
    self.run_process()

  def run_process(self):
    " Run processes with arguments "
    proc_num = len(self.processes)

    for i in range(proc_num):
      if self.processes[i] > 0:
        process = Process(target=self.run_thread, args=(i,))
        try:
          process.start()
        except:
          print("Oops, process didn't start")

  def run_thread(self, current_proc):
    " Run threads with arguments "
    thrd_num = len(self.threads[0])
    count = [self.threads[current_proc][i] for i in range(thrd_num)]

    if thrd_num > 0:
      for i in range(thrd_num):
        if count[i] > 0:
          thread = Thread(target=self.payload_runner, args=(current_proc, i, count[i],))
          try:
            thread.start()
          except:
            print("Oops, thread didn't start")
    else:
      self.payload_runner(current_proc, None, self.processes[current_proc])

  def payload_runner(self, current_proc, current_thrd, count):
    " Run payload inside a thread or process "
    print("Process:", current_proc, "Thread:", current_thrd, "Count:", count)
    for _ in range(count):
      self.run_payload()

  def run_payload(self):
    " Run user's payload with time_sleep interval "
    @sleep_interval(sleep_time=self.sleep_time)
    def _run():
      c = Counter(self.counter)
      global_count = c.global_counter()
      try:
        user_payload(global_count)
      except:
        print("Oops, something wrong in your payload.py")
    return _run()
