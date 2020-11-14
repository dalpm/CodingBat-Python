def missing_char(str, n):
  if (n == 0):
    return str[1:]
  elif (n == (len(str)-1)):
    return str[:len(str)-1]
  else:
    str = str[:n] + str[n+1:]
    return str
