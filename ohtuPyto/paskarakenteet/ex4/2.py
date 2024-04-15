from one import Stack

def check_balance(text):
    stack = Stack()
    check = ('{[(','}])')
    count = 0
    
    for c in text:
        if c in check[0]:
            stack.push(c)
            openIndex = text.find(c)
        if c in check[1]:
            if not stack.pop() == check[0][check[1].find(c)]:
                return f'Match error at position {openIndex+1}'
            count+=1
    if len(stack) > 0:
        return text.rfind(stack.peek())
    else:
        return f'Ok - {count}'

# Test
print(check_balance("a(b)c(([d][e{f}])g)("))