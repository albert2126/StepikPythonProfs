nums = sorted([int(s) for s in input().split()])
print(*sorted(set([nums[i] for i in range(len(nums) - 1) if nums[i] == nums[i+1]])))
