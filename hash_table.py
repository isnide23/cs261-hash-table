# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# YOUR NAME

class HashTable:

    def __init__(self, size = 10):
        self.size = size
        self.data = []

        i = 0
        while i < self.size:
            self.data.append([])
            i += 1

    def __getitem__(self, key):
        index = hash(key) % 10
        return self.data[index]
        
    def __setitem__(self, key, value):
        index = hash(key) % 10
        self.data[index] = [key, value]

    def hash(self, key):
        hash_value = hash(key) 
        print(hash_value)
        return hash_value
        


       
         
        



    

    
        
    
    
        


