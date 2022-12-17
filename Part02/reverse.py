n, x, y, a, b = (int(s) for s in input().split())
nums = list(range(n+1))
nums = nums[:x] + nums[y:x-1:-1] + nums[y+1:]
print(*(nums[1:a] + nums[b:a-1:-1] + nums[b+1:]))
