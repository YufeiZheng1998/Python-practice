def arrayPairSum(nums):
    n = int(len(nums)/2)
    sorted_nums = sorted(nums)
    sum = 0
    i =0
    k = 1
    while i < n:
        sum += sorted_nums[len(nums)-1-k]
        k+=2
        i+=1
    return sum
print(arrayPairSum([1,3,2,6]))