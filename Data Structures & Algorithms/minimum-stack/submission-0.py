class MinStack:

    def __init__(self):
        self.MinStack = []
    # every function should run in O(1) time complexity
    # need to have self in front of everything because 
    # self refers to the current instance of that class, so everytime you want to change 
    # the object you need to access
    # and let python know you want to alter that specfic instance 
        
    def push(self, val: int) -> None:
        self.MinStack.append(val)

    def pop(self) -> None:
        del self.MinStack[-1]

    def top(self) -> int:
        return self.MinStack[-1]

    def getMin(self) -> int:
        current_min = float('inf')
        for m in self.MinStack: 
            if m < current_min: 
                current_min = m 
        
        return current_min
