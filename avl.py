# import bunny_tree
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
#         self.height=1
# class AVL:
#     def __init__(self):
#         self.root=None
#     def height(self,root):
#         if root is None:
#             return 0
#         return root.height
#     def right_rotate(root):
#         x=root.left
#         y=x.right
#         x.right=root
#         root.left=y
#         return x
    
#     def left_rotate(root):
#         x=root.right
#         y=x.left
#         x.left=root
#         root.right=y
#         return x
#     def _insert(self,data,root):
#         if root is None:
#             return Node(data)
#         if data<root.data:
#             root.left=self._insert(data,root.left)
#         elif data>root.data:
#             root.right=self._insert(data, root.right)
#         root.height=max(self.height(root.left),self.height(root.right))+1
#         print(root.height,"--",self.balnced(root))
#         b=self.balnced(root)
#         if b>1 and data<root.left.data:#rr
#             return self.right_rotate(root)
#         if b>1 and data>root.left.data:#lr
#             root.left=self.left_rotate(root.left)
#             return self.right_rotate(root)
#         if b<-1 and data>root.right.data:#ll
#             return self.left_rotate(root)
#         if b<-1 and data<root.right.data:#rl
#             self.right=self.right_rotate(root.right)
#             return self.left_rotate(root)
#         return root
           
#     def insert(self,data):
#         if self.root is None:
#             self.root=Node(data)
#             return 
#         self.root=self._insert(data,self.root)
       
#     def balnced(self,root):
#         if root is None:
#             return 0
#         return self.balnced(root.left)-self.balnced(root.right)
#     def _display(self,root):
#         if root is  None:
#             return
#         self._display(root.left)
#         print(root.data)
#         self._display(root.right)
#     def display(self):
#         self._display(self.root)
   
#     def parent_child(self,parent,p=None):
#         if parent is None:
#             return []
#         l=[]
#         if p is not None:
#             l.append((p.data,parent.data))
#         l.extend(self.parent_child(parent.left,parent))
#         l.extend(self.parent_child(parent.right,parent))
#         return l

# a=AVL()
# a.insert(2)
# a.insert(4)
# a.insert(10)
# a.insert(3)
# a.insert(34)
# a.insert(7)
# a.insert(36)
# a.insert(50)
# a.insert(11)
# a.display()
# data=a.parent_child(a.root)
# print(data)
# bunny_tree.di_draw_tree(data)

import bunny_tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return 0
        return root.height

    def right_rotate(self, root):
        x = root.left
        y = x.right
        x.right = root
        root.left = y

        root.height = max(self.height(root.left), self.height(root.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1

        return x

    def left_rotate(self, root):
        x = root.right
        y = x.left
        x.left = root
        root.right = y

        root.height = max(self.height(root.left), self.height(root.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1

        return x

    def _insert(self, data, root):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self._insert(data, root.left)
        elif data > root.data:
            root.right = self._insert(data, root.right)

        root.height = max(self.height(root.left), self.height(root.right)) + 1
        print(root.height, "--", self.balanced(root))  # Retained as per original code
        b = self.balanced(root)

        if b > 1 and data < root.left.data:  # RR
            return self.right_rotate(root)
        if b > 1 and data > root.left.data:  # LR
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if b < -1 and data > root.right.data:  # LL
            return self.left_rotate(root)
        if b < -1 and data < root.right.data:  # RL
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        self.root = self._insert(data, self.root)

    def balanced(self, root):
        if root is None:
            return 0
        return self.height(root.left) - self.height(root.right)

    def _display(self, root):
        if root is None:
            return
        self._display(root.left)
        print(root.data)
        self._display(root.right)

    def display(self):
        self._display(self.root)

    def parent_child(self, parent, p=None):
        if parent is None:
            return []
        l = []
        if p is not None:
            l.append((p.data, parent.data))
        l.extend(self.parent_child(parent.left, parent))
        l.extend(self.parent_child(parent.right, parent))
        return l

a = AVL()
a.insert(2)
a.insert(4)
a.insert(10)
a.insert(3)
a.insert(34)
a.insert(7)
a.insert(36)
a.insert(50)
a.insert(11)

a.display()

data = a.parent_child(a.root)
print(data) 

bunny_tree.di_draw_tree(data)
