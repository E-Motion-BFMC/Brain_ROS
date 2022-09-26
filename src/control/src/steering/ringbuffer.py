#!/usr/bin/env python3

import collections

class ringbuffer:
    def __init__(self, size):
        self._data = collections.deque(maxlen=size)

    def push(self, data):
        self._data.append(data)

if __name__ == '__main__':
    ringbuffer = ringbuffer(2)
    for i in range(4):
        ringbuffer.push(i)
    print(ringbuffer._data)
