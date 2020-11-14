def combo_string(a, b):
  if (len(a) == 0) and (len(b) == 0):
    return []
  elif len(a) > len(b):
    str = b + a + b
    return str
  elif len(a) < len(b):
    str = a + b + a
    return str
