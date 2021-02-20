ops = input().split()
stack = []

for op in ops:
    if op == '+':
        op2 = stack.pop()
        op1 = stack.pop()
        stack.append(op1 + op2)
    elif op == '-':
        # ['3', '4', '-'] should be '-1'
        op2 = stack.pop()
        op1 = stack.pop()
        stack.append(op1 - op2)
    elif op == '*':
        op2 = stack.pop()
        op1 = stack.pop()
        stack.append(op1 * op2)
    else:
        stack.append(int(op))

print(stack.pop())
