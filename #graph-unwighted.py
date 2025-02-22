#graph

class graph:
    def __init__(self):
        self.vertex={}
    def add_edge(self,start,end):
        if start not in self.vertex:
            self.vertex[start]=[end]
        else:
            self.vertex[start]+=[end]
        if end not in self.vertex:
            self.vertex[end]=[start]
        else:
            self.vertex[end]+=[start]
    def display(self):
        print(self.vertex)
    def find_route(self,start,end,path=[]):
        path=path+ [start]
        if start == end:
            return [path]
        if start not in self.vertex:
            return []
        paths=[]
        for no in self.vertex[start]:
            if no not in path:
                npaths=self.find_route(no,end,path)
                for p in npaths:
                    paths.append(p)
        return paths

    def bfs(self,start):
        queue=[start]
        visited=[]
        while len(queue)!=0:
            item=queue.pop(0)
            if item not in visited:
             visited.append(item)
            for no in self.vertex[item]:
                if no not in visited:
                    queue.append(no)
        print(visited)            
    def dfs(self,start,visited=[]):
        visited+=[start]
        for i in self.vertex[start]:
            if i not in visited:
                self.dfs(i,visited)
        return visited
        
g=graph()
g.add_edge('b','f')
g.add_edge('a','b')
g.add_edge('a','c')
g.add_edge('b','d')
g.add_edge('d','c')
g.add_edge('e','f')
g.add_edge('b','c')
g.display()
for i in g.find_route('a','d',[]):
    print(i)
    pass
g.bfs('a')
print(g.dfs('a'))
