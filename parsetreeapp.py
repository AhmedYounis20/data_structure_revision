import operator
from datasection import binarytree,stack

def buildparsetree(expression):
    fplist=expression.split()
    etree=binarytree('')
    dadstack=stack()
    dadstack.push(etree)
    current = etree
    for i in fplist :
        if i == '(':
            dadstack.push(current)
            current.insert_left('')
            current=current.getleft()
        elif i not in "+-/*)":
            current.setval(int(i))
            current=dadstack.pop()
        elif i in '+-*/' :
            current.setval(i)
            dadstack.push(current)
            current.set_right('')
            current=current.getright()
        elif i == ')':
            current=dadstack.pop()
    return etree
def preorder(tree):
    if tree != None:
        print(tree.getval(),end='')
        preorder(tree.getleft())
        preorder(tree.getright())
def evaluateparse(tree):
    operators={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    left=tree.getleft()
    right=tree.getright()
    if left and right:
        operation=operators[tree.getval()]
        return operation(evaluateparse(tree.getleft()),evaluateparse(tree.getright()))
    else :
        return tree.getval()

t= buildparsetree('( ( 3 + 5 ) + ( 5 * 2 ) )')
print(evaluateparse(t))


