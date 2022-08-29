def is_valid(string) -> int:
    symbols, stack = {"(": ")", "{": "}", "[": "]"}, []
    for s in string:
        if s in symbols:
            stack.append(s)
        elif len(stack) == 0 or symbols[stack.pop()] != s:
            return False
    return len(stack) == 0


print(is_valid("(){{[]}}"))
print(is_valid("()[{]}"))
