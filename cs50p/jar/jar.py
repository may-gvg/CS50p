class Jar:

    def __init__(self, capacity=12):
        self.size2 = 0
        capacity = int(capacity)
        if capacity < 1:
            raise ValueError
        self.capacity2 = capacity

    def __str__(self):
        return self.size2 * "🍪"


    def deposit(self, n):
        if self.size2 + n > self.capacity2:
            raise ValueError
        self.size2 = self.size2 + n
        #return self.size2

    def withdraw(self, n):
        if n > self.size2:
            raise ValueError
        self.size2 = self.size2 - n
        #return self.size2

    @property
    def capacity(self):
        return self.capacity2

    @property
    def size(self):
        return self.size2
