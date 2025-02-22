'''def join(l,m,r):
    lindex=m-l+1
    rindex=r-m
    left=[arr[l+i] for i in range(lindex)]
    right=[arr[m+1+i] for i in range(rindex)]
    #print(l,r)
    i=j=0
    k=l
    while i<lindex and j<rindex:
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while i<lindex:
        arr[k]=left[i]
        k+=1
        i+=1
    while j<rindex:
        arr[k]=right[j]
        k+=1
        j+=1    
def split(s,e):
    if s>=e:
       return
    m=(s+e)//2
    split(s,m)
    split(m+1,e)
    join(s,m,e)
arr=[80,20,90,40,10,50]
split(0,len(arr)-1)
print('merge sort',arr)
arr=[80,20,90,40,10,50]
'''

import random
import time

def pivot(s,e):
    pi=arr[e]
    n=s-1
    for i in range(s,e):
        if arr[i]<=pi:
            n+=1
            arr[n],arr[i]=arr[i],arr[n]
    arr[e],arr[n+1]=arr[n+1],arr[e]
    return n+1
        
def quick(s,e):
   if s<e:
    pi=pivot(s,e)
    quick(s,pi-1)
    quick(pi+1,e)
a=9000
l=[]
for _ in range(10):
    st=time.time()
    a+=10000
    l.append([])
    for i in range(3):
        arr=[random.randint(0,1000) for i in range(a)]
        quick(0,len(arr)-1)
        #l[_].append(f"Time for taking {a} length array running is {int(time.time())-int(st)}ms")
        print(f"Time for taking {a} length array running is {int(time.time())-int(st)}ms")
