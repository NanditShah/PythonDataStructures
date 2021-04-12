class Hashmap:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100
    def add(self,key,value):
        h = self.get_hash(key)
        found = False
        
        for index,element in enumerate(self.arr[h]):
            if element[0] == key and len(element) == 2:
                self.arr[h][index] = (key,value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))
        
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        found = False
        for index , element in enumerate(self.arr[h]):
            if element[0] == key and len(element) == 2:
                self.arr[h][index] == (key,value)
                found = True
                break
        if not found :
            self.arr[h].append((key,value))
                
                
    def get(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
            
            
    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        for index,element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][index] = 
            
    def print_hm(self):
        values = [i for i in self.arr if i != []]
        return values



hm = Hashmap()
hm.add('march 9',110)
hm.add('dec 17',78)
hm.add('march 21',4545)

hm['march 12'] = 108
print(hm.get('march 9'))
print(hm['march 12'])
print(hm['march 21'])

hm.print_hm()