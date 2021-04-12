# Class For Single Node Which Stores Data and the next Node
class Node:
    def __init__(self ,data=None, next=None):
        self.data = data
        self.next = next


# Class That Implements LL

class LinkedList:
    def __init__(self):
        self.head=None
        
        
        
#   Printing Whole LL
    def print_ll(self):
        if self.head is None:
            print('Linked list is empty')
            return
        temp = self.head
        ll_str = ''
        while temp:
            ll_str += str(temp.data)+' --> ' if temp.next else str(temp.data)
            temp=temp.next
        print(ll_str)
        
        
        
#   For Getting Length of LL
    def get_length(self):
        if self.head is None:
            print("The Length is 0")
            return 0
        temp=self.head
        count = 0
        while temp:
            temp=temp.next
            count += 1
        return count
  


#   For Inserting Values At the begining of the LL
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node
        
        
        
#   For Inserting Values at the end of LL    
    def insert_at_end(self,data):
        if self.head is None:
            self.insert_at_begining(data)
            return
        temp = self.head
        
        while temp.next:
            temp=temp.next
        temp.next = Node(data,None)
        
        
                
#   For Inserting Value at given Index(starting from 0)
    def insert_at(self,index,data):
        if index<0  or index > self.get_length():
            raise Exception("Invalid Index")
        
        if self.head is None or index == 0:
            self.insert_at_begining(data)
            return
        temp = self.head
        count = 0
        while temp:
            
            if count == index - 1:
                nxt_node = temp.next
                temp.next = Node(data,nxt_node)
                break
            temp=temp.next
            count += 1

            
            
#   For Inserting list of Values to the End of LL
    def insert_values(self,data_list):
        
        for data in data_list:
            self.insert_at_end(data)
        
        
        
    
#     For Removing Values at given indext(Starting from 0)
    def remove_at(self,index):
        if index<0  or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return
        temp = self.head
        count = 0
        while temp: 
            if count == index - 1:
                temp.next = temp.next.next
                break
            temp = temp.next
            count += 1        

ll = LinkedList()
ll.insert_at_begining(5)
ll.insert_at_begining(10)
ll.insert_at_end(0)
ll.insert_at_end(-5)
ll.insert_at_end(-10)
ll.insert_at(0,10)
ll.insert_at(3,12)
ll.print_ll()

ll.remove_at(3)
ll.print_ll()

ll.insert_values([1,2,3,4,5])
ll.print_ll()

print(f'The length is {ll.get_length()}')


ll2 = LinkedList()

ll2.insert_at_begining("Nandit")
ll2.insert_at_begining("Shah")
ll2.insert_at_end('Suhagkumar')
ll2.print_ll()

ll2.remove_at(1)
ll2.insert_at(1,'Shail')

ll2.print_ll()