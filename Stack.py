class Stack:
    def __init__(self):
        self.stack = []
        
    def pop(self):
        if self.is_empty():
            return
        
        return self.stack.pop()
  
    def push(self,data):
        self.stack.append(data)
    
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    def get_peek(self):
        return self.stack[-1]
    
    def print_stack(self):
        print_str = ''
        if self.is_empty() is False:
            for element in self.stack:
                    print_str += str(element) + '---'
            print(print_str)
        else:
            print('Stack is Empty')
            


s_l_v = Stack()

s_l_v.push(5)
s_l_v.push(10)
s_l_v.push(15)
s_l_v.push(15)
s_l_v.push(15)
s_l_v.push(15)
s_l_v.push(15)


s_l_v.pop()

print(s_l_v.get_peek())

s_l_v.print_stack()

print(s_l_v.is_empty())



import collections

class Stack:
    
    def __init__(self):
        self.stack = collections.deque()
    
    def push(self,data):
        self.stack.append(data)
        
    def pop(self):
        if self.is_empty():
            return
        return self.stack.pop()
        
    def is_empty(self):
        if len(self.stack) == 0 :
            return True
        else:
            return False
    def get_peek(self):
        return self.stack[-1]
        
    def print_stack(self):
        print_str = ''
        if self.is_empty() is False:
            for element in self.stack:
                print_str += str(element)+'---'
            print(print_str)
        else:
            print('List is Empty')


s_d_v = Stack()

s_d_v.push(5)
s_d_v.push(10)
s_d_v.push(15)
s_d_v.push(15)
s_d_v.push(15)
s_d_v.push(15)
s_d_v.push(15)


s_d_v.pop()

print(s_d_v.get_peek())

s_d_v.print_stack()

print(s_d_v.is_empty())