import random

print("Welcome to the Numaster Game!")

while True:

    print("\nChoose Difficulty: ")
    print("1. Easy (1-10, 5 tries)")
    print("2. Medium (1-50, 7 tries)")
    print("3. Hard (1-100, 10 tries)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        number = random.randint(1,10)
        attempts = 5
    elif choice == '2':
        number = random.randint(1,50)
        attempts = 7
    elif choice == '3':
        number = random.randint(1,100)
        attempts = 10
    else:
        print("Invalid Choice, Try Again.")
        continue

    score = 0

    while attempts > 0:
        guess = int(input("Guess the number:"))

        if guess == number:
            print("Congratulations! You guessed the correct number!")
            score = attempts * 10
            print("Your score is:", score)
            break
        elif guess < number:
            print("Too Low! Try Again")
        else:
            print("Too High! Try Again")

            attempts -= 1
            print("Attempts left:", attempts)

    if attempts == 0:
        print("Game Over! The correct number was:", number)

    play_again = input("Do you want to play again? (yes/no): ")

    if play_again.lower() != 'yes':
        print("Thank you for playing Numaster! Goodbye!")
        break



