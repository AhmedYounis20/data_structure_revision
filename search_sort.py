def binary_while(alist,item):
    first=0
    last=len(alist)-1
    while(first<=last):
        mid=(last+first)//2
        if alist[mid]==item:
            return str(mid+1)
        elif alist[mid] < item :
            first=mid+1
        else :
            last=mid-1
    return 'not found'
a=[23,4,1,4,1,24,6,7]
def binary_recursion(alist,item):
    first=0
    last=len(alist)-1
    while(first<=last):
        mid=(first+last)//2
        if alist[mid]==item:
            return 'found'
        elif alist[mid] < item :
            return binary_recursion(alist[mid+1:],item)
        else :
            return binary_recursion(alist[:mid],item)
    return 'not found'
def ordinary_bubble_sort(alist):
    n=len(alist)
    for passage in range(n-1,0,-1):
        for i in range(0,passage-1):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]

def smart_bubble_sort(alist):
    n=len(alist)
    exchange=True
    for passage in range(n-1,0,-1):
        if exchange=='False':
            break;
        exchange=False
        for i in range(passage):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
                exchange=True
def selection_sort(alist):
    for i in range(len(alist)-1):
        min=alist[i]
        pos=i
        for j in range(i+1,len(alist)):
            if alist[j]<min:
                min= alist[j]
                pos=j
        alist[i],alist[pos]=min,alist[i]
def merge_sort(alist):
    print('spliting: ',alist)
    if len(alist)>1:
        mid=len(alist)//2
        left=alist[:mid]
        right=alist[mid:]
        merge_sort(left)
        merge_sort(right)
        i=0
        j=0
        k=0
        while(i < len(left) and j < len(right)):
            if left[i]<right[j]:
                alist[k]=left[i]
                i+=1
            else :
                alist[k]=right[j]
                j+=1
            k+=1
        while i <len(left):
            alist[k]=left[i]
            i+=1
            k+=1
        while j < len(right):
            alist[k]=right[j]
            j+=1
            k+=1
        print('merging:',alist)
def quicksort(alist):
    quickhelper(alist,0,len(alist)-1)
def quickhelper(alist,first,last):
    if first<last:
        splitpoint=partition(alist,first,last)
        quickhelper(alist,first,splitpoint-1)
        quickhelper(alist,splitpoint+1,last)
def partition(alist,first,last):
    pivotvalue=alist[first]
    leftmark=first+1
    rightmark=last
    done=False
    while not done :
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark+=1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark-=1
        if rightmark <leftmark:
            done=True
        else:
            alist[leftmark],alist[rightmark]=alist[rightmark],alist[leftmark]
        alist[first],alist[rightmark]=alist[rightmark],alist[first]
    return rightmark
def insertion_sort(alist):
    for li in range(1,len(alist)):
        currentvalue=alist[li]
        position=li
        while position>0 and alist[position-1] > currentvalue:
            alist[position]= alist[position-1]
            position-=1
        alist[position]=currentvalue




quicksort(a)
print(a)




