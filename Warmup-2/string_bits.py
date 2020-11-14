def string_bits(str):
  a = ""
  for i in range(len(str)):
    if i % 2 == 0:
      a = a + str[i]
  return a
