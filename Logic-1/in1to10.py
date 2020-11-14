def in1to10(n, outside_mode):
  if outside_mode == False and (1 <= n <= 10):
    return True
  elif outside_mode == True and (1 < n < 10) == False:
    return True
  else:
    return False
