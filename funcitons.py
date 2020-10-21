
#%%
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return (a * x*x) + (b * x) + c
evalQuadratic (1,2,3,4)

# %%
def f(x,y):
    x = x + y
    print ("In f(x,y) : x and y: ",x ,y)
    return x
x = 2
y = 2
f(x,y)

# %%

def a(x):
    return x + 1 
a(a(a(6)))

# %%
def a(x, y, z):
     if x:
         return y
     else:
         return z
a(3>2,a,b)
# %%

def b(q, r):
    return a(q>r, q, r)
b(2,3)
# %%
x = 12
def g(x):
    x = x + 1
    def h(y):
        return x + y
    return h(6)
g(x)
# %%

str1 = "exterminate!"
#str1.count('e')
#str1.upper
#str1.upper()
str1 = str1.replace('e','*')
str1
# %%
str2 = "number one - the larch"
#str2 = str2.capitalize()
#str2.swapcase()
str2.find('')
#str2.replace("one", "seven")
#str2.find('!')


# %%
str = "basically that is not that hard"
str.replace('that', 'which')


# %%
#Recursive method for iteration
def multi(base,exp):
    if exp <= 0:
        return 1
    else:
        return base * multi(base, exp-1)
multi(-1.99,0)
# %%
"""
Write an iterative function iterPower(base, exp)
 that calculates the exponential base,exp by simply
  using successive multiplication. For example, 
  iterPower(base, exp) should compute base,exp by 
  multiplying base times itself exp times.
  Write such a function below. 
"""

def iterPower(base,exp):
    result = 1
    while exp > 0:
        result *= base
        exp -= 1 
    return result
iterPower(4,5)



# %%

def gcd(a,b):
    '''
    a and b is positive integer value
    returns: a positive interger the greated common divisor of a and b.
    '''
    testvalue = min(a, b)
    while a % testvalue != 0 or b % testvalue != 0:
        testvalue -= 1 
    return testvalue
gcd(9,12)

# %%
#This is the recursive solution to find the GCD between two integers a and b
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b,a%b)
gcdRecur(9,12)


# %%
