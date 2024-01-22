from my_class import Stack

my_stack = Stack()
def string_test(test_string: str) -> print():
    my_dict = {'[':']','(':')','{':'}',']':'[',')':'(','}':'{'}
    for item in test_string:
        if my_stack.is_empty():
            my_stack.push(item)
            continue
        if item == my_dict[my_stack.peek()]:
            my_stack.pop()
        else:
            my_stack.push(item)

    if my_stack.size() == 0:
        result = 'Сбалансированно'
    else:
        result = 'Несбалансированно'
    return print(result)