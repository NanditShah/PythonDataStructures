import collections

class Queue():
    def __init__(self):
        self.queue = collections.deque()
        
    def enque(self,data):
        self.queue.appendleft(data)
    
    def deque(self):
        if self.is_empty():
            return
        return self.queue.pop()
    
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False
    
    def print_queue(self):
        print_str = ''
        if self.is_empty():
            print('Queue is empty')
            return
        for element in self.queue:
            print_str = print_str + str(element) +"<---"
        print(print_str)



q = Queue()
q.enque(2)
q.enque(12)
q.enque(22)
q.enque(32)

q.print_queue()

q.deque()