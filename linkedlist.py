class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def setdata(self,data):
        self.data=data
    def getdata(self):
        return self.data
    def setnext(self,node):
        self.next=node
    def getnext(self):
        return self.next
class Unorderedlist:

    def __init__(self):
        self.head=None
    def add(self,data):
        temp=Node(data)
        temp.setnext(self.head)
        self.head=temp
    def search(self,item):
        current=self.head
        found = False
        while current != None:
                if current.getdata() == item:
                    return True

                else:
                    current=current.getnext()
        return False
    def remove(self,item):
        if self.search(item):
            current=self.head
            previous= None
            found = False
            while not found :
                if current.getdata()==item :
                    found = True
                else :
                    previous=current
                    current=current.getnext()
            if previous == None:
                self.head=current.getnext()
            else :
                previous.setnext(current.getnext())
    def printlist(self):
        current=self.head
        print('#################')
        while current != None :
            print(current.getdata(),end=' ')
            current=current.getnext()
        print('#################')
        ####################################################
class orderedlist:
    def __init__(self):
        self.head=None
    def add(self,data):
        current=self.head
        previous=None
        while current != None:
            if current.getdata()> data:
                break
            else :
                previous=current
                current=current.getnext()
        temp=Node(data)
        if previous == None:
            temp.setnext(self.head)
            self.head=temp
        else:
            temp.setnext(current)
            previous.setnext(temp)
    def search(self,item):
        current=self.head
        while current != None:
            if current.getdata() == item:
                return True
            else:
                if current.getdata() > item :
                    return False
                else:
                    current=current.getnext()
        return False
    def remove(self,item):
        if self.search(item):
            current=self.head
            previous= None
            found = False
            while not found :
                if current.getdata()==item :
                    found = True
                else :
                    previous=current
                    current=current.getnext()
            if previous == None:
                self.head=current.getnext()
            else :
                previous.setnext(current.getnext())