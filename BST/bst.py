#bst
class node:
    def __init__(self,data) -> None:
        self.data=data
        self.right=None
        self.left=None
class BST:
    def __init__(self) -> None:
        self.root=None
    def insert(self,parent,item):
        if parent is None:
            return node(item)
        elif parent.data>item:
            parent.left=self.insert(parent.left,item)
        else:
           parent.right=self.insert(parent.right,item) 
        return parent
    def inorder(self,parent):
     if parent is not None:
        self.inorder(parent.left)
        print(parent.data,end=' ')
        self.inorder(parent.right)
    def postorder(self,parent):
     if parent is not None:
        self.postorder(parent.left)
        self.postorder(parent.right)
        print(parent.data)
    def preorder(self,parent):
        return self._preorder(parent,[])
    def _preorder(self,parent,list):
      if parent is not None:
        list.append(parent.data)
        self._preorder(parent.left,list)
        self._preorder(parent.right,list)
        return list
    def BFS(self,parent):
     list=[parent]
     l_c=r=0
     while len(list)!=0:
        parent=list.pop(0) 
        print(parent.data,end=' ')
        if parent.left is not None:
            list.append(parent.left)
            l_c+=1
        if parent.right is not None:
            list.append(parent.right)
            r+=1
    def previse(self):
        self.prev=None
    def search(self,parent,item):
        if parent.data==item:
            print("elememt found : ",parent.data,self.prev.data)
            return parent,self.prev
        elif parent.data<item:
            if parent.right is None:
                print("element is not in tree")
                return -1,-1
            self.prev=parent
            self.search(parent.right,item)
        else:
            if parent.left is None:
                print("element is not in tree")
                return -1
            prev=parent
            self.search(parent.left,item)
            
    def parent_child(self,parent,p=None):
        if parent is None:
            return []
        l=[]
        if p is not None:
            l.append((p.data,parent.data))
        l.extend(self.parent_child(parent.left,parent))
        l.extend(self.parent_child(parent.right,parent))
        return l
    def level(self,parent):
        if parent is None:
            return -1
        return max(self.level(parent.right),self.level(parent.left))+1
    def delete(self,parent,item):
        '''if parent.data==item:
            if parent.left is None:
                return parent.right
            elif parent.right is None:
                return parent.left
            list= self.preorder(parent.left)
            print(list)
            for i in list[1:]:
                self.insert()
            return parent.left
        self.previse()
        out=self.search(parent,item)
        if out==-1:
            print("element not found")
            return
        #l-rotation
        if out.right is  None:
           pass 
        '''
        list= self.preorder(parent)
        print(list,'---')
        if item not in list:
            print("element not in tree")
            return parent
        parent=None
        print(list)
        if list[0]==item:
            list.pop(0)
        parent=self.insert(parent,list[0])
        for i in list[1:]:
            if i==item:
                continue
            self.insert(parent,i)
        return parent
            
        
obj=BST()
parent=None
parent=obj.insert(parent,10)
print(parent.data)
obj.insert(parent,5)
obj.insert(parent,11)
obj.insert(parent,7)
obj.insert(parent,-1)
obj.insert(parent,6)
obj.insert(parent,9)
obj.insert(parent,13)
obj.insert(parent,4)
obj.insert(parent,0)
obj.insert(parent,100)
obj.insert(parent,50)
obj.insert(parent,1)
print('---')
obj.inorder(parent)
print('\n',obj.preorder(parent))
print('----')   
obj.BFS(parent)
obj.search(parent,50)
obj.search(parent,1000)
print(obj.level(parent))
#parent=obj.delete(parent,10)
print("--after delete--")
print(obj.preorder(parent))
#parent=obj.delete(parent,13)
obj.inorder(parent)
print('\n ----- ')
data=obj.parent_child(parent)
print(data)


import networkx as n
import matplotlib.pyplot as plt

g=n.DiGraph()
g.add_edges_from(data)
pos=n.spring_layout(g)
n.draw(g,pos=pos,with_labels=True)
plt.title('root '+str(parent.data))
plt.show()
