from random import randint

# int("tulip", 36) * int("punda", 36) * int("tenzin", 36) * int("jahin", 36) = 125425943660100159598652166029422   
n = int("tulip", 36) * int("punda", 36) * int("tenzin", 36) * int("jahin", 36)
secret = randint(0, n)

if __name__ == "__main__":
    guess = -1
    
    while guess != secret:
        try:
            guess = int(input("Guess! "))
            
            if (guess < secret):
                print("Higher!")
            elif (guess > secret):
                print("Lower!")

        except ValueError as e:
            print("You broke something! :(")
    
    print("You win!")