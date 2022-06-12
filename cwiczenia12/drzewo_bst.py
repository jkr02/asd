class Node:
    def __init__(self, val):
        self.val=val
        self.parent=None
        self.left=None
        self.right=None
def next(node):
    if node.right:
        return minimum(node.right)
    v=node
    while v.parent is not None:
        if v.parent.left==v:
            return v.parent
        v=v.parent
    return None