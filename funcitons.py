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
