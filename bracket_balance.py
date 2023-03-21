from stack import Stack


def brackets_balanced(some_brackets: str) -> str:

    result = True

    size = len(some_brackets)
    all_opened = ('[', '(', '{')
    all_closed = (']', ')', '}')

    if size % 2 != 0:
        result = False

    stack = Stack()
    for bracket in some_brackets:
        if bracket in all_opened:
            stack.push(all_opened.index(bracket))
        elif bracket in all_closed:
            if stack.peek() == all_closed.index(bracket):
                stack.pop()
            else:
                result = False
        else:
            raise ValueError('Character not supported for this check')

    if result:
        return "Сбалансировано"
    else:
        return "Несбалансировано"
