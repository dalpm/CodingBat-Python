def max_end3(nums):
  if nums[0] > nums[-1]:
    a = nums[0]
    for i in range(3):
      nums[i] = a
  else:
    a = nums[-1]
    for i in range(3):
      nums[i] = a
  return nums
