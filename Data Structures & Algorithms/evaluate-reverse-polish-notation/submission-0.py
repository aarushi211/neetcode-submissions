class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ["+", "-", "*", "/"]
        stack = []

        for token in tokens:
            if token in operations:
                num1 = stack.pop()
                num2 = stack.pop()

                if token == "+":
                    stack.append(num1+num2)
                elif token == "-":
                    stack.append(num2-num1)
                elif token == "*":
                    stack.append(num1*num2)
                elif token == "/":
                    stack.append(int(float(num2)/num1))
            else:
                stack.append(int(token))
        return stack[0]
            