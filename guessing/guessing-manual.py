from random import randint

# Smaller range (15941) for manual guessing
n = int("cat", 36)
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