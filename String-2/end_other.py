def end_other(a, b):
  a = a.lower()
  b = b.lower()
  if len(a) > len(b):
    if b == a[len(a)-len(b):]:
      return True
    else:
      return False
  elif len(a) < len(b):
    if a == b[len(b)-len(a):]:
      return True
    else:
      return False
  elif len(a) == len(b):
    if a == b:
      return True
    else:
      return False
