class MyDocket:
    def __init__(self, list) -> None:
        self.names = list
        self.index = len(list)
    
    def __iter__(self):
        return self
       
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        else:
            self.index = self.index - 1
            return self.names[self.index]
       
       
if __name__ == '__main__':
    s = [1, 2, 3, 4, 5]
    obj = MyDocket(s)