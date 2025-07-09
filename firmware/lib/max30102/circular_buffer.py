class CircularBuffer:
    def init(self, size):
        self.size = size
        self.buffer = [0] * size
        self.index = 0
    
    def add(self, value):
        self.buffer[self.index] = value
        self.index = (self.index + 1) % self.size

    def get(self):
        return self.buffer

    def is_full(self):
        return all(v != 0 for v in self.buffer)

    def mean(self):
        return sum(self.buffer) / len(self.buffer)

    def stddev(self):
        m = self.mean()
        return (sum((x - m) ** 2 for x in self.buffer) / len(self.buffer)) ** 0.5
