# Normal Solution
def addDigits(num):
    i = 0
    digits = []
    sum = 0
    while num > 0:
        digits.append(num % 10)
        num = num // 10
        i = i + 1
    for i in digits:
        sum += i
    if sum / 10 >=1:
        return addDigits(sum)
    else:
        return sum
print(addDigits(38))


# Another Solution
#  每步对num /10 然后加上个位上的数字； 然后再对这个加起来的数字处理，其实就可以类比每一步得到大于10的数然后继续处理。
#  分成了 n 个零散物品， 然后这n个零散物品还是可以再继续分类（>10），然后再对这n个零散物品继续分类成n'.....
#  然后最后其实得到的小于10的数字就是我们需要的结果。也其实就是对最后的个位进行处理
def addDigits_supreme(num):
    return (num-1) % 9 +1
