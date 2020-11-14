def front3(str):
  if len(str) < 3:
    str = str * 3
    return str
  else:
    str= str[:3] * 3
    return str
