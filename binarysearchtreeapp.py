from datasection import BST
tree=BST()
for i in range(10):
    print(tree.size)
    tree.add(i,i*2)
for i in range(0,10):
    print(tree.valueof(i))
    tree.remove(i)
    print('size became:',tree.size)

