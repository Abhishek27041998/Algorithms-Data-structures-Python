"""
This is an implementation of Queue
"""


class Queue:
    def __init__(self, max_size=5):
        self.queue = []
        self.front = 0
        self.rare = 0
        self.size = max_size

    def enqueue(self, element):
        if self.rare == self.size:
            return "Queue is Full"
        else:
            self.queue.append(element)
            self.rare += 1

    def is_empty(self):
        if self.front == self.rare:
            return True
        else:
            return False

    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"
        else:
            elem = self.queue[self.front]
            self.front += 1
            return elem

    def front_element(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.queue[self.front]

    def size_of_queue(self):
        return self.rare - self.front

    def print_elements(self):
        for elem in self.queue:
            print(elem)


if __name__ == '__main__':
    queue = Queue(5)

    # Enqueue elements
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print('-----------')
    print('Queue Elements')
    queue.print_elements()

    # Dequeue element
    print('-----------')
    print(f'Dequeued element : {queue.dequeue()}')

    # Size
    print('-----------')
    print(f'Size: {queue.size_of_queue()}')

    # Front element
    print('------------')
    print(f'Front Element: {queue.front_element()}')

    # Enqueue elements
    print('-------------')
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.enqueue(3))

    # Dequeue elements
    print('-------------')
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    print(queue.dequeue())
