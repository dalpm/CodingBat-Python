def rotate_left3(nums):
  num_new = [0,0,0]
  num_new[0] = nums[1]
  num_new[1] = nums[2]
  num_new[2] = nums[0]
  return num_new
