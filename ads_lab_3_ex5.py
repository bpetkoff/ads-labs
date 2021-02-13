"""
This file contains the reversed queue function
"""

class Empty(Exception):
    """Shows an error on attempt to access an element from an empty container."""
    pass

class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10  # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue"""
        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """
        Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty
        """

        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """
        Remove and return the first element of the qieie (i.e. FIFO)

        Raise Empty exception if the queue is empty.
        """

        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None  # clear the cell
        self._front = (self._front + 1) % len(self._data)  # change the front pointer to the next cell
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to the back of the queue"""
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        """
        Resize to a new list of capacity >= len(self).
        """
        old = self._data  # keep track of existing list
        self._data = [None]*cap  # allocate list with new capacity
        walk = self._front
        for k in range(self._size):     # only consider existing elements
            self._data[k] = old[walk]  # intentionally shift indices
            walk = (1 + walk) % len(old)  # use old size as modulus
        self._front = 0  # front has been realigned




if __name__ == '__main__':
    Q = ArrayQueue()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)
    Q.enqueue(5)
    print(Q._data)
    Q.enqueue(6)
    Q.enqueue(7)
    Q.enqueue(8)
    Q.enqueue(9)
    Q.enqueue(10)
    print(Q._data)
    Q.dequeue()
    Q.dequeue()
    Q.dequeue()
    Q.dequeue()
    Q.dequeue()
    print(Q._data)
    Q.enqueue(11)
    Q.enqueue(12)
    Q.enqueue(13)
    print(Q._data)





def reverse_queue(queue):
    """
    This is the function that takes a
     queue as an input and reverses it
    """
    reversed_queue = ArrayQueue()
    old_front = queue._front
    old_size = queue._size
    old_len = len(queue._data)
    e = ((old_front + old_size) % old_len) - 1
    print(e)
    for i in queue._data:
        reversed_queue.enqueue(queue._data[e])
        e -= 1
    return reversed_queue._data

W = reverse_queue(Q)

print(W[0])
print(Q._data)
print(Q.dequeue())


