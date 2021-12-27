from helpers.locker import Locker


class Counter(Locker):

    def __init__(self, counter):
        super().__init__()
        self.counter = counter

    def global_counter(self):
        self.lock_proc()
        self.lock_thread()
        self.counter.value += 1
        self.unlock_thread()
        self.unlock_proc()
        return self.counter.value
