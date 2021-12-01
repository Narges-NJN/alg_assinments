
precedence = {
        '(': 0,
        '+':1, '-':1, '<':1, '>':1,
        '*':2, '/':2,
        '^':3,
}

class Expression_Evaluator:
    def __init__(self, input):
        print("Expression:", input)
        self.tokens = input.split()
        self.value_stk = []
        self.operation_stk = []

    def eval_exp(self):
        
        for t in self.tokens:
            if t.isdigit():
                self.value_stk.append(int(t))
                continue
            elif t == '(':
                self.operation_stk.append(t)
                continue
            elif t == ')':
                while self.operation_stk:
                    op = self.operation_stk.pop()
                    if op == '(':
                        break
                    self.do_op(op)
                continue

            self.repeat_op(t)

        while self.operation_stk:
            op = self.operation_stk.pop()
            if op == '(':
                raise Exception('Mismatched opening parenthesis!')
            self.do_op(op)
        
        return self.value_stk.pop()
        

    def repeat_op(self,t):
        prec_t = precedence[t]
        while self.operation_stk and prec_t <= precedence[self.operation_stk[-1]]:
            op = self.operation_stk.pop()
            self.do_op(op)
        self.operation_stk.append(t)

            
    def do_op(self, op):
        y = self.value_stk.pop()
        x = self.value_stk.pop()
        if op == '-': self.value_stk.append(x - y)
        elif op == '+': self.value_stk.append(x + y)
        elif op == '<': self.value_stk.append(1 if x < y else 0)
        elif op == '>': self.value_stk.append(1 if x > y else 0)
        elif op == '*': self.value_stk.append(x * y)
        elif op == '/': self.value_stk.append(x // y)
        elif op == '^': self.value_stk.append(x ** y)
        

if __name__ == "__main__":
    #expression = input('Enter expression: ')
    expression = '2 ^ ( 1 + 3 ^ 2 )'
    exp = Expression_Evaluator(expression)
    print(f"Result: {exp.eval_exp()}")