import numpy as np

class OrderedVector:
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=int)

    # O(n)
    def print(self):
        if(self.last_position == -1):
            print('Vector is empty')
        else:
            for i in range(self.last_position + 1):
                print(i, ' - ', self.values[i])

    def insert(self, value):
        if self.last_position == self.capacity - 1
            print('Maximum capacity')
            return

        position = 0
        for i in range(self.last_position + 1):
            position = i
            if self.values[i] > value:
                break
            
        x = self.last_position
        while x >= position:
            self.values[x+1] = self.values[x]
            x -= 1

        self.values[position] = value
        self.last_position += 1
