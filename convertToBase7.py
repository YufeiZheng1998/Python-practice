def convertToBase7(num):
    if num==0:
        return '0'
    positive = True
    num_base7 = ''
    if num<0:
        positive = False
        num = abs(num)
    while num != 0:
        num_base7+=str(num%7)
        num = int(num / 7)
    if not positive:
        num_base7+='-'
    return num_base7[::-1]