from multiprocessing import Lock as Plock
from threading import Lock as Tlock


class Locker:

    def __init__(self):
        self.plock = Plock()
        self.tlock = Tlock()

    def lock_proc(self):
        """ Lock execution in others process """
        return self.plock.acquire()

    def unlock_proc(self):
        """ Unlock execution in others process """
        return self.plock.release()

    def lock_thread(self):
        """ Lock execution in others thread on current process """
        return self.tlock.acquire()

    def unlock_thread(self):
        """ Unlock execution in others thread on current process """
        return self.tlock.release()
