#graph-weighted

import bunny_tree as b

class Graph:
    def __init__(self):
        self.graph={}
    def add(self,e1,e2,cost):
        if e1 not in self.graph:
            self.graph[e1]=[(e2,cost)]
        else:
            self.graph[e1]+=[(e2,cost)]
        if e2 not in self.graph:
            self.graph[e2]=[(e1,cost)]
        else:
            self.graph[e2]+=[(e1,cost)]
    def display(self):
        #print(self.graph)
        return self.graph
    def adj(self):
        tep=self.graph
        en=list(enumerate(sorted(set([i for i in tep]+[j[0]  for i in tep for j in tep[i]]))))
        en=dict(((j,i) for i,j in en))
        print(en)
        zero=[[0 for i in range(len(en))]for j in range(len(en))]
        for t in tep:
          for k in tep[t]:
            zero[en[t]][en[k[0]]]=k[1]
        for i in zero:
            print(i)
    
    def find_all_paths(self,start,end):
        return self.find_all_paths_((start,0),end,[])
    def find_all_paths_(self,start,end,path):
        path=path+[start]
        if start[0]==end:
            return [path]
        if start[0] not in self.graph:
            return []
        paths=[]
        for no in self.graph[start[0]]:
            if no not in path:
                p=self.find_all_paths_(no,end,path)
                paths+=[i for i in p]
        return paths
    
    
    def find_the_minal_path_length(self,start,end):
        h=0
        d={}
        p=self.find_all_paths(start,end)
        for i in p:
            c=0
            s=''
            for j,k in i:
               c+=k
               s+=j+'--'
            p[h]=s[:-2]
            d[c]=h
            h+=1
        print(min(d))
        path=p[d[min(d)]]
        return path,min(d)
        
    
    def minimal_spanning_cost(self,start):
        #primis
        l_c=[]
        t_l=[]
        g_l=[]
        minimal=0
        self.final_l=[]
        visited=[start]
        tep=self.graph
        en=list(enumerate(sorted(set([i for i in tep]+[j[0]  for i in tep for j in tep[i]]))))
        while len(visited)!=len(en):
            print(1)
            if start in tep:
             for i in tep[start]:
               if i[0] not in visited:
                t_l.append(i[0])
                g_l.append(start)
                l_c.append(i[1])
            minimal+=min(l_c)
            count=0
            for i in l_c:
                if i==min(l_c):
                    break
                count+=1
            start=t_l[count]
            if start not in visited:
             visited.append(t_l[count])
             self.final_l.append((t_l[count],min(l_c),g_l[count]))
            l_c[count]=float('inf')
        #print(final_l)
        return minimal,visited
g=Graph()
g.add('a','b',12)
g.add('a','c',24)
g.add('c','d',13)
g.add('y','X',0)
g.add('d','e',21)
g.add('b','d',26)
g.add('b','e',12)
g.add('f','e',8)
g.add('f','g',5)
g.add('a','g',3)
g.display()
g.adj()
for i in g.find_all_paths('a','e'):
    c=0
    for j,k in i:
        c+=k
        #print(j+'--',end='')
    #print("value of path is :",c)
print("shortest path from two dist",g.find_the_minal_path_length('a','g'))
print(g.minimal_spanning_cost('d'))

x=g.display()
#print(x)
l=[(i,j[0],j[1])  for i in x for j in x[i]]
#print(l)
b.draw_tree_weighted(l)

data=[(k,i,j) for i,j,k in g.final_l]
#print(data)
b.draw_tree_weighted(data)
