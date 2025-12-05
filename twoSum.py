def twoSum(nums, target):
    seen = {}
    
    for i in range(len(nums)):
        num = nums[i]
        diff = target - num
        
        if diff in seen:
            return [seen[diff], i]
        
        seen[num] = i

nums = [5, 2, 7, 15]
target = 9

print(twoSum(nums, target))