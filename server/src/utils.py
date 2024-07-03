import time
class Helper():
    def __init__(self, start_timestamp = time.time()) -> None:
        self.prev_time_stamp = start_timestamp
    def have_x_sec_passed(self, x = 5):
        has_passed = False
        current_timestamp = time.time()
        if (self.prev_time_stamp < current_timestamp - x):
            self.prev_time_stamp = current_timestamp
            has_passed = True
        return has_passed