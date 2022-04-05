class Stack:
    def __init__(self, input_i):
        self.input_i = list(input_i)

    def isEmpty(self):
        if len(self.input_i) == 0:
            return True
        else:
            return False

    def push(self, new_item):
        self.input_i.reverse()
        self.input_i.append(new_item)
        self.input_i.reverse()

    def pop(self):
        if len(self.input_i) > 0:
            return self.input_i.pop(0)
        else:
            return 'Нулевой список'

    def peek(self):
        return self.input_i[0]

    def size(self):
        return len(self.input_i)


if __name__ == "__main__":
    b = '(((([{}]))))()()'
    e = ''
    stack = Stack(b)
    stack_e = Stack(e)

    if stack.peek() == r'\)*\}*\]*' or stack.size() % 2 == 1:
        print('Несбалансированно')
    else:
        while stack.size() != 1:
            stack_e.push(stack.pop())
            if stack.peek() == r'\)*\}*\]*' and stack_e.peek() == r'\(*\{*\[*':
                stack.pop()
                stack_e.pop()
        else:
            print('Сбалансировано')
