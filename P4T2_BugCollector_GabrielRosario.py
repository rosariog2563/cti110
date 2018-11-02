# Collecting Bugs
# 30 Oct 2018
# CTI-110 P4T2 - Bug Collector
# Gabriel Rosario
#

totalDays = 5
totalNumberOfBugs = 0

for currentDay in range( 1, totalDays + 1 ):
    bugsCollected = int( input("How many bugs were collected on day " + \
                               str( currentDay ) + ": " ) )
    totalNumberOfBugs += bugsCollected
print('\nThe total number of bugs collected for all', totalDays, 'days is', \
      totalNumberOfBugs )
