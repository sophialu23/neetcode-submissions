class TimeMap:
    # all timestamps are always going to be increasing 

    def __init__(self):
        # initialize the hashmap 
        self.store = {} # key= string, value= [list of values]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store: 
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.store.get(key, [])
        # we want to binary search the result 
        left = 0 
        right = len(values) - 1
        while left <= right: # always <=
            middle = (left + right) // 2 # integer division 
            if values[middle][1] <= timestamp: 
                result = values[middle][0]
                left = middle + 1 
            else: 
                # this is invalid > time cant be greater because always increasing 
                # cant do continue as that will create infinite loop 
                # it would continue to calculate the same middle forever 
                right = middle - 1 
        return result 
                
            

        