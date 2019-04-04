# Ground shipping function
def gs_cost(weight):
  if weight <= 2.0:
    return 20.0 + 1.5 * weight
  elif weight <= 6.0:
    return 20.0 + 3.0 * weight
  elif weight <= 10.0:
    return 20.0 + 4.0 * weight
  else:
    return 20.0 + 4.75 * weight
  
#Test gs_cost
#print(gs_cost(8.4))

#Premium ground shipping variable (fixed cost)
pgs_cost = 125.0

# Drone shipping function
def ds_cost(weight):
  if weight <= 2.0:
    return 4.5 * weight
  elif weight <= 6.0:
    return 9.0 * weight
  elif weight <= 10.0:
    return 12.0 * weight
  else:
    return 14.25 * weight

#Test ds_cost
#print(ds_cost(1.5))