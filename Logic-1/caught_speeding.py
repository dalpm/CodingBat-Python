def caught_speeding(speed, is_birthday):
  if is_birthday == False:
    x = speed
  elif is_birthday == True:
    x = speed - 5
  if x <= 60:
    return 0
  elif 61 <= x <= 80:
    return 1
  elif 81 <= x:
    return 2
