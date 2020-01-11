def search(nums, target):
    left = 0
    right = len(nums) - 1
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1

print(search([5], 5))