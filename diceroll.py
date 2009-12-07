# roll -- A dice-rolling application that rolls a given number of dice
#  (between 2-9) a given number of times, and then keeps track of the 
#  average of the totals of the two highest rolls in each set.

import sys
import random 

# Start the loop

# Define the Grand Total

grand_total = 0

# Take in the number of rolls

try:
	nor = sys.argv[2]
except:
	sys.exit("Usage: roll <number of dice> <number of times>")

for i in range(int(nor)):

# Make sure an argument is given when the program is run

    try:
        nop = len(sys.argv)
    except:
        sys.exit("roll -- A dice rolling application that rolls 2-9 d6 and adds the highest two values.\nUsage: roll <number of dice>.")

    if nop != 3:
        sys.exit("roll -- A dice rolling application that rolls 2-9 d6 and adds the highest two values.\n\nUsage: roll <number of dice> <number of times>")

# Take in the number of d6 to be rolled, ensuring something is entered

    try:
        nod = sys.argv[1]
    except:
        sys.exit("Usage: roll <number of dice> <number of times>")


# Make sure nod is a number between 2 and 9.
    r = range(2,10)
    if (int(nod) not in r):
         sys.exit("Please enter a number of dice between 2 and 9.")

# Roll the dice "nod" number of times
    dr = [random.randint(1, 6) for i in xrange(int(nod))]

# Sort the list
    
    dr.sort()

# Pop off the top two values from the list and store them seperately

    highest = dr.pop()
    
    next_highest = dr.pop()
#
    total = highest + next_highest

# Combine the totals into grand_total

grand_total = grand_total + total

# Print the results

print "You rolled " + nod + " d6 " + str(nor) + " times, and I took the highest two scores from each roll."
print "..."
print "The grand total of your " + str(nor) + " rolls was: " + str(grand_total)
# Create and print the average

avg = grand_total / float(nor)
print "The average total was: " + str(avg)
