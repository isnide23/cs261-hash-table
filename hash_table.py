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
        index = hash(key) % self.size
        if self.data[index] == []:
            return None
        else:
            return self.data[index][0][1]
   
    def __setitem__(self, key, value):
        index = hash(key) % self.size
        for i in self.data[index]:
            if i[0] == key:
                i[1] = value 
                return        
        self.data[index].append([key,value]) 

        # for x in self.data:
        #     if x[index][0] == key:
        #         x[index][1] = value
        #         return index
        # self.data[index].append([key, value])

        # index = hash(key) % self.size
        # self.data[index].append([key, value])
        # print(self.data)

        # if self.data[index] == []:
        #     self.data[index].append([key, value])
        # elif self.data[index] != []:
        #     self.data[index][0] = [key, value]
        # else:
        #     self.data[index].append([key, value])

    def hash(self, key):
        hash_value = hash(key) % self.size
        print(hash_value)
        return hash_value

    # def delete(self, key):
    #     index = self.hash(key)
    #     self.data[index][0] 
        


       
         
        



    

    
        
    
    
        


