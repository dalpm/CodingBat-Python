def sum67(nums):
  sum = 0
  is_6 = False
  for i in range(len(nums)):
    if nums[i] == 6:
      is_6 = True
    if is_6 == False:
      sum += nums[i]
    if nums[i] == 7 and is_6:
      is_6 = False
  return sum