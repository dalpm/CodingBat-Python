def last2(str):
  count = 0
  if len(str) < 2:
    return 0
  else:
    for i in range(len(str)-1):
      if str[len(str)-2:len(str)] == str[i:i+2]:
        count += 1
    return count - 1
