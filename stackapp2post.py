from datasection import stack
def in_to_post(infix):
    post=[]
    ops=stack()
    op_weight={'(':1,
               '+':2,
               '-':2,
               '*':3,
               '/':3,
               '^':4,
               }
    for degit in infix:
        if degit in 'ASDFGHJKLZXCVBNMQWERTYUIOP' or degit in '1234567890':
            post.append(degit)
        elif degit =='(':
            post.append(degit)
        elif degit==')':
            token=ops.pop()
            while token != '(':
                post.append(token)
                token=ops.pop()
        else :
            while(not ops.IsEmpty() and op_weight[ops.peek()] >= op_weight[degit]) :
                post.append(ops.pop())
            ops.push(degit)
    while not ops.IsEmpty():
        post.append(ops.pop())
    return ''.join(post)

a=in_to_post('A+B-2*1')
print(a)