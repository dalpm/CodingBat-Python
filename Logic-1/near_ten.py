def near_ten(num):
  if 0 <= num % 10 <= 2 or 8 <= num % 10:
    return True
  else:
    return False
