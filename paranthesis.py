def x(expression):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if stack[-1] == bracket_pairs[char]:
                stack.pop()
            else:
                return False
    
    return not stack

# Example usage:
expression = input()
print("Is parenthesized:", x(expression))
