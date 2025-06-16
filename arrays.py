class Array:
    def __init__(self, size):
        self._data = [0] * size

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __str__(self):
        return str(self._data)
