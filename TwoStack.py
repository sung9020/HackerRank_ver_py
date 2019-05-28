class MyQueue(object):
    def __init__(self):
        self.new_stack = []
        self.old_stack = []
    def peek(self): # pop peak 순간에만 최신화 시켜준다. - 시간 단축
        if len(self.new_stack) > 0:
            return self.new_stack[-1]
        else:
            while self.old_stack:
                self.new_stack.append(self.old_stack.pop())
            return self.new_stack[-1]

    def pop(self):
        if len(self.new_stack) > 0 :
            return self.new_stack.pop()
        else:
            while self.old_stack:
                self.new_stack.append(self.old_stack.pop())
            return self.new_stack.pop()

    def put(self, value):
        self.old_stack.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())

