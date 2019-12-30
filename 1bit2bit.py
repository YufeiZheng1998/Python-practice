def isOneBitCharacter(bits):
    index = 0
    last = len(bits)-1
    while last - index >= 2:
        if bits[index] == 0:
            index += 1
        elif bits[index] ==1:
            index += 2
    if index == last:
        return True
    else:
        if bits[index] == 0:
            return True
        else:
            return False
isOneBitCharacter([1,0,0])