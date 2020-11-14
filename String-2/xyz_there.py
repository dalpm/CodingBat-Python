def xyz_there(str):
  str = str.lower()
  count = 0
  for i in range(len(str)):
    if str[i:(i+3)] == "xyz" and (str[i-1] != "."):
      count += 1
  if count > 0:
    return True
  else:
    return False