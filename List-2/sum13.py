def sum13(nums):
  sum = 0
  nums.append(0)
  for i in range(len(nums)):
    if nums[i] == 13:
      nums[i] = 0
      nums[i+1] = 0
  for i in range(len(nums)):    
    sum += nums[i]
  return sum
