print("*****************************")
print("Welcome to the guessing game!")
print("*****************************")

secret_number = 35

user_input = int(input("Type a number: ", ))
print("You typed ", user_input)

user_won = user_input == secret_number
higher = user_input > secret_number
lesser = user_input < secret_number

if(user_won):
    print("You won! :)")
else:
    if(higher):
        print("You guess was higher")
    elif(lesser):
        print("You guess was lesser")

print("End of game")