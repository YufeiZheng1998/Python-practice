def findContentChildren(g, s):
    sorted_g = sorted(g)
    sorted_s = sorted(s)
    i,j = 0,0
    num = 0
    num_g = len(g)
    num_s = len(s)
    while i < num_g:
        flag = False
        while j< num_s:
            if sorted_g[i] <= sorted_s[j]:
                j+=1
                num+=1
                flag = True
                break
            else:
                j+=1
        i += 1
        if not flag:
            break
    return num

print(findContentChildren([1,2,3], [1,1]))