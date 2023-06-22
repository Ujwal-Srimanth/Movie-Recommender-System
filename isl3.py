import random
import numpy as np
from functools import reduce
import time
x=1
class node:
    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.next = None
        self.down = None
class SkipList:
    def __init__(self):
        self.head = node(None, None)
        self.ple = 1
    def insert(self, min, max):
        level = 1
        while random.random() < 0.5:
            level += 1
        if level > self.ple:   
            for i in range(level - self.ple):
                new_head = node(None, None)      
                new_head.down = self.head  
                self.head = new_head
            self.ple = level
        curr = self.head     
        path = []
        while curr:
            if curr.next is None or curr.next.min > min:
                path.append(curr)
                curr = curr.down
            elif curr.next.min == min:
                if curr.next.max==max:
                    return
                elif curr.next.max>max:
                    curr=curr
                    path.append(curr)
                    break
                else:                                         
                    while True:
                        if curr.next is None:
                            break
                        elif curr.next.max<max and curr.next.min==min:
                            curr=curr.next
                        else:
                            break
            elif curr.next.min < min:
                curr = curr.next
        down = None
        while path:
            curr = path.pop()
            new_node = node(min, max)
            new_node.down = down        
            down = new_node
            new_node.next = curr.next
            curr.next = new_node
    def delete(self, min):
        curr = self.head
        while curr:
            if curr.next is None or curr.next.min >= min[0] :
                if curr.next and (curr.next.min == min[0] and curr.next.max==min[1]) :
                    curr.next = curr.next.next
                curr = curr.down
            else:
                curr = curr.next
    def search(self, min,max):
        finallist=[]
        count=0
        curr = self.head
        curr1=self.head
        while curr:
            if curr.next is None:
                curr = curr1.down
                curr1=curr1.down
                count+=1
            elif curr.next.min > min:
                curr=curr.down
            elif curr.next.min <= min and curr.next.max >= max:
                finallist.append([curr.next.min,curr.next.max])
                curr=curr.next
                count+=1
            else:
                curr = curr.next
        if len(finallist)!=0:
            ans = reduce(lambda re, x: re+[x] if x not in re else re, finallist, [])
            print("the range (",min,",",max,") is present in",ans)    
        print("the number of comparsions done for (",min,",",max,") are",count)
    def display(self):
        list=[]
        curr = self.head
        i=self.ple
        while curr:
            temp = curr.next
            print("level ",i,":",end=" ")
            i=i-1
            while temp:
                print("(",temp.min,",",temp.max,")",end="->")
                temp = temp.next
            print()
            curr = curr.down
class BST:
    def __init__(self,data,skip):
        self.data=data
        self.skip=None
        self.right=None
        self.left=None
    element=[]
    def add_child(self,data):
        if data==self.data:
            return
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BST(data,None)
        if data>self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BST(data,None)
    def display_helper(self):
        BST.element.clear()
        BST.element.append(self.skip)
        BST.element.append(self.left.skip)
        BST.element.append(self.left.left.skip)
        BST.element.append(self.left.right.skip)
        BST.element.append(self.right.skip)
        BST.element.append(self.right.left.skip)
        BST.element.append(self.right.right.skip)
        return BST.element
def bui(elements):
    root=BST(elements[0],None)
    for i in range(len(elements)):
        root.add_child(elements[i])
    return root
def search_helper(root,min,max):
    if root is None:
        return
    else:
        m=root.data
        if m[0]<=min and m[1]>=max:
            print("hi")
            root.skip.search(min,max)
        else:
            search_helper(root.left,min,max)
            search_helper(root.right,min,max)
def display_helper2(root):
    element=root.display_helper()
    a=0
    for i in element:
        print(a+1)
        a=a+1
        i.display()
def insert_helper(skipList3,skipList1,skipList2,skipList4,skipList5,skipList6,skipList7):
    min=int(input("input the lower limit"))
    max=int(input("enter the upper limit"))
    st = time.time()
    if(min >=1 and max<1000):
        skipList3.insert(min,max)
    elif(min >=1000 and max<10000):
        skipList2.insert(min,max)
    elif(min>=10000 and max<25000):
        skipList4.insert(min,max)
    elif(min>=25000 and max<=50000):
        skipList1.insert(min,max)
    elif(min>=50000 and max<=75000):
        skipList6.insert(min,max)
    elif(min>=75000 and max<=100000):
        skipList5.insert(min,max)
    else:
        skipList7.insert(min,max)
def delete_helper(root,min,max):
    if root is None:
        return
    else:
        m=root.data
        if m[0]<=min and m[1]>=max:
            l=[min,max]
            root.skip.delete(l)
            return
        delete_helper(root.left,min,max)
        delete_helper(root.right,min,max)

# get the start time

elements=[[25000,50000],[1000,10000],[1,1000],[10000,25000],[75000,100000],[50000,75000]]
tree=bui(elements)
exception=BST([1,100000],None)
tree.right.right=exception
skipList1=SkipList()
skipList2=SkipList()
skipList3=SkipList()
skipList4=SkipList()
skipList5=SkipList()
skipList6=SkipList()
skipList7=SkipList()
tree.skip=skipList1
tree.left.skip=skipList2
tree.left.left.skip=skipList3
tree.left.right.skip=skipList4
tree.right.skip=skipList5
tree.right.left.skip=skipList6
tree.right.right.skip=skipList7
while(True):
    choice=int(input("enter a choice"))
    print("1) for insert")
    print("2) for delete")
    print("3) for display")
    print("4) for search")
    print("5) for exit")
    if choice==1:
        insert_helper(skipList3,skipList1,skipList2,skipList4,skipList5,skipList6,skipList7)
    elif choice==3:
        display_helper2(tree)
    elif choice==4:
        print("enter the element u r searching for")
        a=int(input("enter the lower range"))
        b=int(input("enter the higher range"))
        search_helper(tree,a,b)
    elif choice==2:
        print("enter the element want to delete")
        a=int(input("enter the lower range"))
        b=int(input("enter the higher range"))
        delete_helper(tree,a,b)
    elif choice==5:
        break


