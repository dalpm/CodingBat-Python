def front_times(str, n):
  if len(str) < 3:
    str = str * n
    return str
  else:
    str = str[:3] * n
    return str
