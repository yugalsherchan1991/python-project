
#%%
x = int(input('Please enter the integer:'))
if x%2 == 0:
    print('')
    print('Even')
else:
    print('')
    print('Odd')
print('Done with conditional expression')


# %%
x = int(input('Please enter the integer'))
if x%2 ==0:
    if x%3 == 0:
        print('No is divisible by 2 and 3')
    else:
        print('No is divisible by 2 but not 3')
elif x%3 == 0:
    print('No is divisible by 3 but not 2 ')
else:
    print('Given value is not divisible')


# %%
for n in range (5):
    print(n)


# %%
n = input("You are in the forest. Go left or right?")
while n == "right":
    n = input("You are lost in the forest. Go left or right")
print("Your are our of the forest. Hurray!")


# %%
numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))


# %%
mysum = int  0 
for i in range (5, 11, 2):
    mysum += i
        mysum == 5
        break
print(mysum)
# %%
n = 11 
while n > 2:
    n -=1 
    if n % 2 == 0: 
        print(n)
# %%
initial = 0 
end = 6
result = 0
while initial < end:
    result = result + initial
    initial +=1 
print(result)
    
     
   
# %%
num = 10 
for num in range(5):
    print(num)
print(num)


# %%
divisor = 2
for num in range(0, 10, 2):
    print(num/divisor)

# %%
for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print("Foo!")

# %%
for letter in 'hola':
    print(letter)

# %%
count = 0 
for letter in "Snow!":
    print('Letter # '+ str(count) + 'is ' + str(letter))
    count +=1
    break
print(count)

# %%
myStr = '6.00x 1'

for char in myStr:
    print(char)

print('done')

# %%
greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')


# %%
school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons)) 
# %%
#Finding the cube root of x 

x = int(input('Enter the integer no:'))
ans = 0 
while ans**3 < x:
    ans += 1
if ans ** 3 != x:
    print(str(x) + " is not a perfect cube.")
else:
    print("The cube root of " + str(x) + " is " + str(ans))

# %%
# These are all same code written in different loops 
teration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 

#%%
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        break
# %%
iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 

# %%

 # This form of loop goes for infinite amount of time 
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        
#%%



count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))


# %%



count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
# %%

count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print("Iteration " + str(iteration) + "; count is: " + str(count))

# This is the end of that example of for and while loop

# %%
#This print the number of vowels in a given string.
s = "aftermathofdestruciton"
numVowels = 0
for char in s:
    if char == "a" or char == "e" or char == "i" or char == "o"\
        or char == "u":
        numVowels +=1
print("Number Of Vowels:" + str(numVowels))

# %%
#This prints the number of vowels and constant in a given string.

newString = 'yugalsherchan'
noOfVowels = 0 
noOfConstant = 0
for char in newString:
    if char == "a" or char == "e" or char == "i" or char == "o"\
        or char == "u":
        noOfVowels += 1
    else:
        noOfConstant +=1
print("Number of constant is:" + str(noOfConstant))    
print(" Number of vowels is:" + str(noOfVowels))

# %%
# How to find the no of times Bob occour in a given sting.
s = "azcbobobegglirakl"
noOfBob = 0
for char in range(len(s)):
    if s[char:char + 3] == "bob":
        noOfBob += 1  
print("No of Bob in this word are:" + str(noOfBob))
# %%
#Find no of times a sting comes in a given word 
nSting = "realgoingforgoingforrealreal"
noOfFor = 0
for char in range(len(nSting)):
    if nSting[char:char+4] == "real":
        noOfFor += 1
print("No of for in the word is:" + str(noOfFor))    


# %%
