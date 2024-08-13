#linked list
class node:
    def __init__(self,data:int):
        self.data=data
        self.next=None
class linkedlist:
    'performing linked list' 
    def __init__(self):
        self.head=None
        self.top=None
    def add(self,item):
     obj=node(item)
     if self.head==None:
        self.head=obj
        self.top=obj
     elif self.head==self.top:
        self.top=obj
        self.head.next=self.top
     else:
            self.tem=self.top
            self.top=obj
            self.tem.next=self.top
    def add_first(self,item):
        obj=node(item)
        if self.head==None:
            self.head=obj
            self.top=obj
        else:
            tep=self.head
            self.head=obj
            obj.next=tep
    def display(self):
        n=self.head
        while n!=None:
         print(n.data)
         n=n.next
    def back_display(self):
        n=self.head
        back=None
        while n!=None:
         n.back=back
         back=n
         #print(self.n.data)
         n=n.next
        dummy=back
        while dummy!=None:
            print(dummy.data)
            dummy=dummy.back
    def peek(self):
        print(self.top.data)
    def pop(self):
        prev=None
        temp=self.head
        while(temp!=None):
            if temp.next!=None:
             prev=temp
            temp=temp.next
        self.top=prev
        self.top.next=None 
    def first_delete(self):
        self.head=self.head.next
obj=linkedlist()
'''obj.add(10)
obj.add(200)
obj.add(300)
obj.display()
obj.peek()
obj.pop()
obj.peek()
obj.add_first(100)
obj.add_first(900)
obj.add(500)
print("----")
obj.display()
obj.first_delete()
print("---------")'''
obj.display()
print('''Write the command :
    for push - add(item),add_first(item)
    for pop - pop(),first_delete()
    for display - display()
    for top element - peek()
    for exit - break or exit
''')
while True:
    prompt=input(">>>").strip()
    if prompt in ['break','exit']:
        print("quit..")
        break
    try:
        eval("obj."+prompt)
    except Exception as e:
        print("Exception :",e,'\n no such operation :',prompt)



