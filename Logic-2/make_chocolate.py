def make_chocolate(small, big, goal):
  num_small = 0
  while goal - (big * 5) < 0:
    big = big - 1
  if goal - (big * 5) > small:
    return - 1
  else:
    num_small = goal - (big * 5)
    return num_small
