def cigar_party(cigars, is_weekend):
  if (is_weekend == False) and (40 <= cigars <= 60):
    return True
  elif (is_weekend == True) and (40 <= cigars):
    return True
  else:
    return False
