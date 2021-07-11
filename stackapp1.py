from datasection import stack
def isvalid(text):
    s=stack()
    for line in text :
        for token in line :
            if token in '{[(':
                s.push(token)
            elif token in '}])':
                if s.IsEmpty():
                    return False
                current=s.pop()
                if (token =='}' and current !='{') or (token == ']' and current != '[' ) or \
                        (token ==')' and current!= '(') :
                    return False
    return s.IsEmpty()
if __name__=='__main__':
    print(isvalid(input()))