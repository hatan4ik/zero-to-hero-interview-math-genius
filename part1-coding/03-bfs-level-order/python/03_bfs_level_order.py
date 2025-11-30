from collections import deque
class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val; self.left=left; self.right=right
def level_order(root):
    if not root: return []
    q,res=deque([root]),[]
    while q:
        lvl=[]
        for _ in range(len(q)):
            n=q.popleft(); lvl.append(n.val)
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
        res.append(lvl)
    return res
