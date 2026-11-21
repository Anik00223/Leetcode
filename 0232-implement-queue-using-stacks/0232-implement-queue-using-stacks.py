class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x):
        self.input_stack.append(x)

    def pop(self):
        self.peek()

        return self.output_stack.pop()

    def peek(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(
                    self.input_stack.pop()
                )

        return self.output_stack[-1]

    def empty(self):
        return not self.input_stack and not self.output_stack