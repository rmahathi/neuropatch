class CircularBuffer:
    def init(self, size):
        self.size = size
        self.buffer = [0] * size
        self.index = 0

    def add(self, value):
        self.buffer[self.index] = value
        self.index = (self.index + 1) % self.size

    def get(self):
        return self.buffer[self.index:] + self.buffer[:self.index]
