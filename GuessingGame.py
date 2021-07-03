import random
number = random.randint(1,9)
guess = int(input("guess a number between 1-10: "))
print(number)
if (guess==number):
    print("Lamo, How...... OK you won!!")
elif(guess==number-1):
    print("very close")
elif(guess==number+1):    
    print("very close")
else:
    print("You searched area51,the goverment shot you, stonks 4 you. Better luck next time.")