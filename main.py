import hanging
import guessit

print("***************************")
print("Choose a game")
print("***************************")

print("1 - Guess it")
print("2 - Hanging")

game = input("What game? ")

if game == "1":
    print("Guess it selected")
    guessit.play()
elif game == "2" :
    print("Hanging selected")
    hanging.play()