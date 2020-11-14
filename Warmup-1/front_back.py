def front_back(str):
  if len(str) == 1:
    return str
  else:
    front = str[:1]
    back = str[len(str)-1:len(str)]
    str = back + str[1:len(str)-1] + front
    return str