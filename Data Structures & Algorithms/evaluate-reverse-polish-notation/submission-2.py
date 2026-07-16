class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ['+', '-', '*', '/']
        for i in tokens:
            if i not in operations:
                stack.append(i)
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
            if i == '+':
                stack.append(num1 + num2)
            if i == '*':
                stack.append(num1 * num2)
            if i == '-':
                stack.append(num2 - num1)
            if i == '/':
                stack.append(num2/num1)
        return int(stack.pop())
