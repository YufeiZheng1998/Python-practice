class TreeNode(object):
 def __init__(self, x):
     self.val = x
     self.left = None
     self.right = None
def averageOfLevels(root):
    if root is None:
        return None
    queue = [root]
    result = []
    while queue:
        out = []
        temp = []
        for t in queue:
            out.append(t.val)
            if t.left:
                temp.append(t.left)
            if t.right:
                temp.append(t.right)
        result.append(float(sum(out))/len(out))
        queue = temp
    return result

