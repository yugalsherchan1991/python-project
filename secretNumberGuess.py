#%%
#This is code to guess a secret number from user input of between the range of 0 to 100 using bisection algorithm

sNumber = (input("Please think of a number between 0 and 100: "))
low = 0
high= 100
guess = 50

while True:
    print("Is your secret number: " + str(guess))
    newInput = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correct")
    if newInput == "h":
        high = guess
        guess = abs((high + low)//2)
    elif newInput == "l":
        low = guess
        guess = abs((high + low)//2)
    elif newInput == "c":
        print("Game over. Your secert number was: " + str(guess))
        break
    elif newInput != "h" and "l" and "c":
        print("Sorry, I did not understand your input.")
  
        









# %%

num1 = int(input())
num2 = int(input())
def solveMeFirst(a,b):
    return num1 + num2
solveMeFirst(num1,num2)




# %%

def solveMeFirst(a,b):

    num1 = int(input())
    num2 = int(input())
    return num1 + num2 
    res = solveMeFirst(num1,num2)

print(solveMeFirst(2,3))



# %%

# %%