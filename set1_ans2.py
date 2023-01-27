def twoSum(nums, target):
    required = {}
    for i in range(len(nums)):
        if target - nums[i] in required:
            return [input_list[required[target - nums[i]]],input_list[i]]
        else:
            required[nums[i]]=i

input_list = list(map(int,input().split()))
target = int(input())

print(twoSum(input_list, target))
