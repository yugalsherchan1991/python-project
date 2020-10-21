'''


We can use the idea of bisection search to determine if a character is in a string,
so long as the string is sorted in alphabetical order.First, test the middle 
character of a string against the character you're looking for (the "test character").
If they are the same, we are done - we've found the character we're looking for!
If they're not the same, check if the test character is "smaller" than the middle 
character. If so, we need only consider the lower half of the string; otherwise, 
we only consider the upper half of the string. (Note that you can compare characters 
using Python's < function.)

Implement the function isIn(char, aStr) which implements the above idea recursively 
to test if char is in aStr. char will be a single character and aStr will be a string 
that is in alphabetical order. The function should return a boolean value.

As you design the function, think very carefully about what the base cases should be.
'''

#%%
def isIn(char,aStr):
    newString = sorted(aStr)
    aStr = "".join(newString)
    if aStr == "":
        return False
    if len(aStr) == 1:
        return char == aStr
    midIndex= [len(aStr)//2]
    mid_char = aStr[len(aStr)//2]
    mid = len(aStr)//2
    if mid_char == char:
        return True
    elif char < mid_char:
        return isIn(char,aStr[:mid])
    else:
        return isIn(char,aStr[mid:])
    
    
isIn("a","yugal")
# %%
# These are the methods to sort a character of string in 
# alphabetical order and then join them.
a = "yugalsherchan"
newA = sorted(a)
a = "".join(newA)
print(a)
print(len(a))
# %%
import math
from math import pi
def polysum (n,s):
  
    tangent = math.tan(pi/n)
    farea = (0.25 * n * s**2)/tangent
    area = round(farea,4)
    perimeter = (n * s)**2
    
    return area + perimeter
polysum(71,7)

# %%
