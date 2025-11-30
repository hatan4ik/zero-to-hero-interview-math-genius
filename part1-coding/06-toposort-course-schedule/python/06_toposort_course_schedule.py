from collections import defaultdict, deque
def topo_sort(n, edges):
    g=defaultdict(list); indeg=[0]*n
    for a,b in edges: g[b].append(a); indeg[a]+=1
    q=deque([i for i in range(n) if indeg[i]==0]); order=[]
    while q:
        u=q.popleft(); order.append(u)
        for v in g[u]:
            indeg[v]-=1
            if indeg[v]==0: q.append(v)
    return order if len(order)==n else None
