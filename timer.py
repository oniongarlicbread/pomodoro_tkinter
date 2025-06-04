import time

import time


class CountdownTimer:
    def __init__(self, seconds):
        self.duration = seconds
        self.original_duration = seconds
        self.running = False
        self.start_time = None

    # display the time remaining
    def show(self):
        # convert seconds to minutes:seconds
        return time.strftime("%M:%S", time.gmtime(self.duration))

    # start the countdown (non-blocking)
    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time()

    # update the timer (call this regularly from GUI)
    def update(self):
        if self.running and self.start_time:
            elapsed = time.time() - self.start_time
            self.duration = max(0, self.original_duration - int(elapsed))

            if self.duration <= 0:
                self.running = False
                return True  # Timer finished
        return False  # Timer still running

    # check if timer is running
    def is_running(self):
        return self.running

    # reset the timer
    def reset(self):
        self.duration = self.original_duration
        self.running = False
        self.start_time = None

    # stop the timer
    def stop(self):
        self.running = False
