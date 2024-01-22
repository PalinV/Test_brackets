class Stack:
    stack = []
    def __int__(self):
        self.stack = []
        Stack.stack.append(self)
    def is_empty(self):
        if self.size():
            return False
        else:
            return True
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if self.is_empty():
            print('Удаление элемента невозможно.Список пуст')
        else:
            return self.stack.pop()
    def peek(self):
        if self.is_empty():
            print('Возврат элемента невозможен.Список пуст')
        else:
            return self.stack[self.size() - 1]
    def size(self):
        return len(self.stack)