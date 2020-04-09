def max_min(*nums):
    max_num = nums[0]
    min_num = nums[0]
    for n in nums:
        if n > max_num:
            max_num = n
        if n < min_num:
            min_num = n
    return max_num, min_num

print(max_min(-1,3,-9,11,3.14,0))
print(max_min(3,5,-8,9))