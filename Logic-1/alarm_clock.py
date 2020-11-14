def alarm_clock(day, vacation):
  x = "7:00"
  y = "10:00"
  z = "off"
  if (1 <= day <= 5) and (vacation == False):
    return x
  elif (1 <= day <= 5) and (vacation == True):
    return y
  elif ((day == 0) or (day == 6)) and (vacation == False):
    return y
  elif ((day == 0) or (day == 6)) and (vacation == True):
    return z
