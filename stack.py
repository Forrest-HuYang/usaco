class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items )

def convert(infixexpr):
    prec = dict()
    prec[")"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    prefix = []
    s = Stack()
    tokenlist = list(infixexpr)
    tokenlist.reverse()
    for token in tokenlist:
        if not token in prec:
            prefix.append(token)
        elif token == ')':
            s.push(token)
        elif token == '(':
            while s.peek() != ')':
                prefix.append(s.pop())
            s.pop()
        else:
            while (not s.isEmpty())\
                    and s.peek() != ')'\
                    and prec[s.peek()] > prec[token]:
                prefix.append(s.pop())
            s.push(token)
    
    while not s.isEmpty():
        prefix.append(s.pop())
    
    prefix.reverse()
    print(prefix)

def get_val(prexp):
    s = Stack()
    tokenlist = list(prexp)
    tokenlist.reverse()
    for token in tokenlist:
        if token.isdigit():
            s.push(token)
        else:
            operand2 = int(s.pop())
            operand1 = int(s.pop())
            result = domath(token,operand1,operand2)
            s.push(result)
    print(s.items)

def domath(op, op1, op2):
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2


#convert('a*b+c*d')
get_val('+*98*76')