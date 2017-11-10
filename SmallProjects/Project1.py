## Luis Chunga
## Project 1
## Doc string descripion of project
"""
This program will use a dart-throwing algorithm to compute pi.
Darts thrown as being inside the circle will be counted.

I will run the program this way:
    python3 yourpgmname  N
where N is the number of darts thrown.
"""

import sys
import math
import random

ndarts = int(sys.argv[1])

# initialize counter variable
total = 0
on_target = 0
off_target = 0

for i in range(ndarts):
    # Generate random numbers between 0 and 1
    x = random.random()
    y = random.random()
    distance = math.sqrt(x*x + y*y)

    # Determine if darts lands inside circle or outside circle
    if distance <= 1:
        on_target += 1
    elif distance > 1:
        off_target += 1
    total += 1

# Since target area is in quadrant I, multiply by 4 to estimate pi
pi_estimate = (on_target/total) * 4

# Print output
print ("Pi Estimate = ", pi_estimate)


