def calci(exp):
    s = exp.split()[-1]
    i = 0

    def helper():
        nonlocal i

        stack = []
        num = 0
        op = '+'

        while i < len(s):
            ch = s[i]

            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '(':
                i += 1
                num = helper()

            if ch in '+-*/)' or i == len(s) - 1:
                if i == len(s) - 1 and ch.isdigit():
                    pass

                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(stack.pop() / num))

                num = 0
                op = ch

                if ch == ')':
                    return sum(stack)

            i += 1

        return f"s = {sum(stack)}"

    return helper()