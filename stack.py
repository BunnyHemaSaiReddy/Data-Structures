# stack

class Stack:
    'IMPLEMENT THE STACK PUNCTIONS'
    def __init__(self,length:int):
        self.length=length
        self.stack=[]
    def isempty(self)->bool:
        if len(self.stack)==0:
            return 1
        return 0
    def isfull(self)->bool:
        if len(self.stack)==self.length:
            return 1
        return 0
    def push(self, item :int )-> str:
        if self.isfull():
            return "overflow"
        self.stack.append(item)
        return "pushed sucessfully"
    def pop(self)->str:
        if self.isempty():
            return "under flow"
        return f"poped element is {self.stack.pop()}"
    def display(self)->str:
        if self.isempty():
            return "empty stack"
        for i in self.stack[::-1]:
            print('+----+')
            print('|',i,'|')
        return '+----+'
    def top(self)->str:
        if self.isempty():
            return "empty stack"
        return f"top elememt is {self.stack[-1]}"
obj=Stack(int(input("enter the stack length : ")))
print('''Write the command :
    for push - push(item)
    for pop - pop()
    for display - display()
    for top element - top()
    for exit - break or exit
''')
while True:
    prompt=input(">>>").strip().lower()
    if prompt in ['break','exit']:
        print("quit..")
        break
    try:
        print(eval("obj."+prompt))
    except Exception as e:
        print("Exception :",e,'\n no such operation :',prompt)
    
