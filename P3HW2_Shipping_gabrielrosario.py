# CTI-110 
# P3HW2 - Shipping Charges   
# Gabriel Rosario   
# 30 Oct 2018
#

userWeightofPackage = int( input('Please enter the weight of the package: '))

if userWeightofPackage <= 2:
     shippingCharges = 1.50
elif userWeightofPackage < 7:
     shippingCharges = 3.00
elif userWeightofPackage < 11:
     shippingCharges = 4.00
else:
     shippingCharges = 4.75

print("\nFor a package weighing " + str( userWeightofPackage ) +\
      ", you'll pay $" + format( shippingCharges, ",.2f" ) + " per pound." )
