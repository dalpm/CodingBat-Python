def not_string(str):
  if (str[:3] == "not") == True:
    return str
  else:
    str = "not " + str
    return str
