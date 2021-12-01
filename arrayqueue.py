test_values1 = [
    2,
    34,
    69,
    5,
    324,
    3,
]

test_value2 = 99

expected = [
    "[2, 34, 69, 5, 324, 3]",
    "[2, 34, 69, 5, 324, 3, 99, None, None, None, None, None]",
    "[None, 34, 69, 5, 324, 3, 99, None, None, None, None, None]",
]


class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self, capacity):
        ArrayQueue.DEFAULT_CAPACITY = capacity
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, element):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = element
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    @property
    def data(self):
        return self._data


if __name__ == '__main__':

    # make a queue with size 6
    array_queue = ArrayQueue(6)

    # test 1 - to check enqueue function
    for i in range(len(test_values1)):
        array_queue.enqueue(test_values1[i])
    result = str(array_queue.data)
    if result == expected[0]:
        print("PASS: %s = %s" % (result, expected[0]))
    else:
        print("FAIL: %s != %s" % (result, expected[0]))
    # end of test 1

    # test 2 - check resize
    # when new element is added,
    # the queue should resize to double size
    array_queue.enqueue(test_value2)
    result = str(array_queue.data)
    if result == expected[1]:
        print("PASS: %s = %s" % (result, expected[1]))
    else:
        print("FAIL: %s != %s" % (result, expected[1]))
    # end of test 2

    # test 3 - check dequeue
    array_queue.dequeue()
    result = str(array_queue.data)
    if result == expected[2]:
        print("PASS: %s = %s" % (result, expected[2]))
    else:
        print("FAIL: %s != %s" % (result, expected[2]))
    # end of test 3
