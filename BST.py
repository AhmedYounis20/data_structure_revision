class BSTNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.right=None
        self.left=None
class BST:
    def __init__(self):
        self.root=None
        self.size=0
    def length(self):
        return self.size()
    def has_key(self,key):
        return self.bstsearch(self.root,key) is not None
    def Valueof(self,key):
        node = self.bstsearch(self.root,key)
        return node.value
    def bstsearch(self,subtree,key):
        if subtree is None:
            return None
        elif subtree.key > key:
            return self.bstsearch(subtree.left)
        elif subtree.key < key:
            return self.bstsearch(subtree.right)
        else :
            return subtree
    def bstminimum(self,subtree):
        if subtree is None:
            return None
        elif subtree.left is None :
            return subtree
        else :
            return self.bstminimum(subtree.left)
    def bstmaximum(self,subtree):
        if subtree is None:
            return None
        elif subtree.right is None :
            return subtree
        else :
            return self.bstminimum(subtree.right)
    def add(self,key,value):
        node =self.bstsearch(self.root,key)
        if node is not None:
            node.value=value
            return False
        else :
            self.root=self.bstinsert(self.root,key,value)
            self.size+=1
            return True

    def bstinsert(self,subtree,key,value):
        if subtree is None :
            subtree = BSTNode(key,value)
        elif key < subtree.key:
            subtree.left=self.bstinsert(subtree.left,key,value)
        else :
            subtree.right=self.bstinsert(subtree.right,key,value)
        return subtree
    def remove(self,key):
        node=self.bstsearch(self.root,key)
        assert node is not None, 'invalid key'
        self.root=self.bstremove(self.root,key)
        self.size-=1
    def bstremove(self,subtree,key):
        if subtree.left is None and subtree.right is None :
            return None
        elif subtree.left is None or subtree.right is None :
            if subtree.left is not None :
                return self.bstremove(subtree.left,key)
            else:
                return self.bstremove(subtree.right,key)
        else :
            successor= self.bstminimum(subtree.right)
            subtree.key=successor.key
            subtree.value=successor.value
            subtree.right=self.bstremove(subtree.right,successor.key)
            return subtree
