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

#Cheapest method function
def cheapest_shipping(weight):
    if (gs_cost(weight) < ds_cost(weight)) and (gs_cost(weight) < pgs_cost):
        print("The cheapest shipping method is Ground Shipping. It will cost you $"+str(gs_cost(weight)))
    elif (ds_cost(weight) < gs_cost(weight)) and (ds_cost(weight) < pgs_cost):
        print("The cheapest shipping method is Drone Shipping. It will cost you $"+str(ds_cost(weight)))
    elif (pgs_cost < ds_cost(weight)) and (pgs_cost < gs_cost(weight)):
        print("The cheapest shipping method is Premium Ground Shipping. It will cost you $"+str(pgs_cost))
    elif (gs_cost(weight) < ds_cost(weight)) and (gs_cost(weight) == pgs_cost):
        print("You can either choose Ground or Premium Ground Shipping. In both case, it will cost you $" + str(pgs_cost))
    elif (ds_cost(weight) < gs_cost(weight)) and (ds_cost(weight) == pgs_cost):
        print("You can either choose Drone or Premium Ground Shipping. In both case, it will cost you $" + str(pgs_cost))
    else:
        print("You can either choose Ground  or Drone Shipping. In both case, it will cost you $" + str(ds_cost(weight)))