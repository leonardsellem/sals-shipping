def gs_cost(weight):
  if weight <= 2.0:
    return 20.0 + 1.5 * weight
  elif weight <= 6.0:
    return 20.0 + 3.0 * weight
  elif weight <= 10.0:
    return 20.0 + 4.0 * weight
  else:
    return 20.0 + 4.75 * weight
  
  print(gs_cost(8.4))