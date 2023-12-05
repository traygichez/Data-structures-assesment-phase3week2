def is_balanced(expression):
    l = []
    condition = True
    
    if len(expression) % 2 != 0:
        return False
    
    for c in expression:
        if condition:
            if c in '{[(':
                l.append(c)
            elif c in '}])' and len(l) > 0:
                last = l.pop()
                match c:
                    case '}':
                        condition = '{' == last
                    case ']':
                        condition = '[' == last
                    case ')':
                        condition = '(' == last
            else:
                condition = False
    
    return condition

expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False 