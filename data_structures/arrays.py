class Array:
    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)

    def delete(self, value):
        if value in self.data:
            self.data.remove(value)

    def access(self, index):
        if index < 0 or index >= len(self.data):
            return None
        return self.data[index]
