# Male Female Percentage
# 29 Oct 2018
# CTI-110 P2HW2 - Male Female Percentage
# Gabriel Rosario
#

males = int( input('Please enter the number of males in the class: '))
females = int( input('Please enter the number of females in the class: '))
totalStudents = males + females

# method 1 
# malePercentage = ( males / totalStudents ) * 100
# femalePercentage = ( females / totalStudents ) * 100

# print("Male percentage: " + str( malePercentage)+"%")
# print("FeMale percentage: " + str( femalePercentage)+"%")

#method 2 
malePercentage = males / totalStudents
femalePercentage = females / totalStudents

print("There are " + str( totalStudents ) + " students in the class. " + \
     format( malePercentage, ".0%" ) + " of them are males and " + \
     format( femalePercentage, ".0%" ) + " of them are females." )

# if   20 students = 100%
# then 4 students  = ?

# if   20 students = 100%
# then 45 students  = ?
