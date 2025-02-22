tree = {
    1:[(2,2),(3,4)],2:[(3,1),(4,7)],3:[(5,3)],4:[(5,1)]
}

print(tree)
val=tree.values()
v=[1,2,3,4,5]
f=[]
for i in tree:
    #print(tree[i][0][0])
    f.extend([[i,d[0],d[1]] for d in tree[i]])
print(f)
f.sort(key=lambda x:x[-1])
print(f)
print(f[0])
vis=[f[0][1]]
for i in range(1,len(f)):
    if f[i][1] not in vis:
        print(f[i])
        vis.append(f[i][1])
    if len(vis)==len(v):
        break
else:
    print(-1)
print(vis)