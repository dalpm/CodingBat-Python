def parrot_trouble(talking, hour):
  if (talking == True) and ((7 <= hour <= 20) == False):
    return True
  else:
    return False