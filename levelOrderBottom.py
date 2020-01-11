def levelOrderBottom(root):
    if not root:
        return []
    stack = [root]
    res = []
    while len(stack) != 0:
        tmp = []
        res_each  = []
        for i in stack:
            res_each.append(i.val)
            if i.left:
                tmp.append(i.left)
            if i.right:
                tmp.append(i.right)
        stack = tmp
        res.insert(0, res_each)
    return res