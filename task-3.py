# task3.py - Utilities demonstrating classes and simple algorithms (>=50 lines)
from datetime import datetime, timedelta

class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, amount=1):
        self.value += amount
        return self.value

    def dec(self, amount=1):
        self.value -= amount
        return self.value

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = datetime.now()

    def stop(self):
        self.end_time = datetime.now()

    def elapsed(self):
        if not self.start_time:
            return None
        end = self.end_time or datetime.now()
        return end - self.start_time

def sliding_window_max(arr, k):
    if not arr or k <= 0:
        return []
    from collections import deque
    dq = deque()
    res = []
    for i, val in enumerate(arr):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and arr[dq[-1]] < val:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(arr[dq[0]])
    return res

def add_days(date_str, days, fmt="%Y-%m-%d"):
    d = datetime.strptime(date_str, fmt)
    new = d + timedelta(days=days)
    return new.strftime(fmt)

def main():
    c = Counter()
    print("Counter start:", c.value)
    c.inc(5)
    print("After inc 5:", c.value)
    t = Timer()
    t.start()
    for _ in range(1000000):
        pass
    t.stop()
    print("Elapsed:", t.elapsed())
    arr = [1,3,5,2,6,2,1,7]
    print("Sliding max (k=3):", sliding_window_max(arr, 3))
    print("Add 10 days to 2025-10-01:", add_days("2025-10-01", 10))

if __name__ == "__main__":
    main()
