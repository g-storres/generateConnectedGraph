import numpy as np


np.set_printoptions(precision = 3, suppress = True)

def checkZeros(i, v):
    n = np.size(v,0)
    nz = list()
    for k in range(n):
        if v[k] != 0 and k != i and k!= (i+1):
            nz.append(k)
    if(nz != []):
        return np.random.choice(nz)
    else:
        return -1
    
def assign(M,i,j,val):
    M[i,j] = val
    M[j,i] = val
    M[j,j] = M[j,j] - val
    M[i,i] = M[i,i] - val

def eig(M):
    if(np.size(M,1) == np.size(M,0)):
        n = np.size(M,1)
        u = np.linalg.eigvalsh(M)
        v = np.zeros(n)
        for i in range(n):
            v[n-i-1] = u[i]
    return v

def sum(v,ind):
    #n = np.size(v,0)
    s = 0
    for i in range(ind):
        s = s + v[i]
    return s


def gen(n,m):
    if(m<n-1):
        return -1
    L = np.zeros([n,n])
    visited = []
    unvisited = list(range(n))
    u = np.random.choice(range(n))
    unvisited.remove(u)
    v = np.random.choice(unvisited)
    assign(L,u,v,-1)
    visited.append(u)
    visited.append(v)
    unvisited.remove(v)
    for i in range(1,m):
        if(i < n-1): #it means that we haven't visited all vertices yes
            got = False
            while not got:
                u = np.random.choice(unvisited)
                v = np.random.choice(visited)
                if(u!=v and L[u,v]==0):
                    assign(L,u,v,-1)
                    visited.append(u)
                    unvisited.remove(u)
                    got = True
        else: #then we can add whatever edge we please
            got = False
            while not got:
                u = np.random.choice(range(n))
                v = np.random.choice(range(n))
                if(u!=v and L[u,v]==0):
                    assign(L,u,v,-1)
                    got = True
                    
    return L
        
def glm(minVertices,maxVertices):
    n = np.random.choice(range(minVertices,maxVertices+1))
    m = n + np.random.choice(range(2,int(n*n/2-3*n/2)))
    return gen(n,m)