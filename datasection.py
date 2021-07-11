class stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def IsEmpty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[-1]
class queue:
    def __init__(self):
        self.queue=[]
    def IsEmpty(self):
        return self.queue== []
    def enqueue(self,item):
        self.queue.insert(0,item)
    def dequeue(self):
        return self.queue.pop()
    def size(self):
        return  len(self.queue)
class binarytree:
    def __init__(self,rootobj):
        self.key=rootobj
        self.right=None
        self.left=None
    def insert_left(self,newnode):
        if self.left==None:
            self.left=binarytree(newnode)
        else :
            t=binarytree(newnode)
            t.left=self.left
            self.left=t.left
    def insert_right(self,newnode):
        if self.right==None:
            self.right=binarytree(newnode)
        else :
            t=binarytree(newnode)
            t.right=self.right
            self.right=t.right
    def getval(self):
        return self.key
    def setval(self,val):
        self.key=val
    def getright(self):
        return self.right
    def getleft(self):
        return self.left
    def set_right(self,val):
        self.right=binarytree(val)
    def set_left(self,val):
        self.left=binarytree(val)
class BST:
    def __init__(self):
        self.root =None
        self.size=0
    def lenght(self):
        return self.size
    def has_key(self,key):
        return self.bstsearch(self.root,key)
    def bstsearch(self,subtree,key):
        if subtree == None:
            return None
        elif subtree.key < key:
            return self.bstsearch(subtree.right,key)
        elif subtree.key > key:
            return self.bstsearch(subtree.left,key)
        else :
            return subtree
    def valueof(self,key):
        node = self.bstsearch(self.root ,key)
        assert not node == None , 'invalid key sir '
        return node.value
    def add(self,key,value):
        node = self.bstsearch(self.root,key)
        if node != None :
            node.value = value
            return False
        else :
            self.root=self.insert(self.root,key,value)
            self.size+=1
            return True
    def insert(self,subtree,key,value):
        if subtree ==None:
             subtree=BStNode(key,value)
        elif subtree.key > key :
             subtree.left=self.insert(subtree.left,key,value)
        else :
             subtree.right=self.insert(subtree.right,key,value)
        return subtree
    def remove(self,key):
        node = self.bstsearch(self.root,key)
        assert  node is not None  ,'invalid key '
        self.root=self.bstremove(self.root,key)
        self.size-=1
    def bstmax(self,subtree):
        if subtree == None :
            return None
        else :
            if subtree.right == None :
                return subtree.key
            else :
                return self.bstmax(subtree.right)
    def bstmin(self,subtree):
        if subtree == None :
            return None
        else :
            if subtree.left == None :
                return subtree.key
            else :
                return self.bstmin(subtree.left)
    def bstremove(self,subtree,key):
        if subtree.key < key:
            subtree.right=self.bstremove(subtree.right,key)
            return subtree
        if subtree.key > key:
            subtree.left=self.bstremove(subtree.left,key)
            return subtree
        else :
            if subtree.left == None  and subtree.right == None   :
                return None
            elif subtree.left == None  and subtree.right != None :
                return subtree.right
            elif subtree.left != None  and subtree.right == None :
                return subtree.left
            else :
                successor=self.bstmin(subtree.right)
                subtree.key=successor.key
                subtree.value=subtree.value
                subtree.right=self.bstremove(subtree.right,key)
                return subtree





class BStNode:

    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.right=None
        self.left=None