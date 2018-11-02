# Area of Rectangles
# D29 Oct 2018
# CTI-110 P3T1
# Gabriel Rosario
#

# Get the diminsion of rectangle 1.
length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))

# Get the diminsion of rectangle 2.
length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))

# Calculate the area of the rectangles.
area1 = length1 * width1
area2 = length2 * width2

# Determine which have the greater area.
if area1 > area2:
     print('Rectangle 1 has the greater area.')
elif area2 > area1:
     print('Rectangle 2 has the greater area.')
else:
     print('Both have the same area.')
