# Tuition Increase
# 2 nov 2018
# CTI-110 P4HW3 - Tuition Increase
# GabrielRosario
#

currentTuition = 8000

print("Year\tTuition\n----\t-------")
for currentYear in range( 1, 6 ):
    currentTuition += ( 3/100 ) * currentTuition
    print( currentYear, "\t$", format( currentTuition, ".2f" ), sep = "" )
