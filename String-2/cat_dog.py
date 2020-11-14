def cat_dog(str):
  count_dog = 0
  for i in range(len(str)-1):
    if str[i:i+3] == "dog":
      count_dog += 1
  count_cat = 0
  for i in range(len(str)-1):
    if str[i:i+3] == "cat":
      count_cat += 1
  if count_dog == count_cat:
    return True
  else:
    return False
  