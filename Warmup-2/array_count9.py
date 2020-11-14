def array_count9(nums):
  count = 0
  for i in range(len(nums)):
    if 9 == nums[i]:
      count += 1
  return count
