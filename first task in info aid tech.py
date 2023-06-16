import random #This random library gives the random number in the range of (start,stop).
def play_game():
    Secret_num=random.randint(1,100) #This Line of code will give the range of the numbers to be generated in between.
    print("welcome to number guessing Game 😁") #Welcome message for player.
    user_name=input("Enter your name :") #Player name.
    print("RULES:") #Rules that are followed in this game and rules are mentioned below.
    print("1. Game is simple an joyful")#1
    print("2. Game has 10 chances to predict the number")#2
    print("3. Don't try to exit the game in middle")#3
    print("4. Finally go and Rock....")#4
    max_attempts=10 #Attempts that have a player in his/her hand.
    attempts=0
    while attempts<max_attempts:
        guess_num=int(input("Enter the Number :")) #Number will be guessed by this line of code
        attempts += 1
        if guess_num>Secret_num: #This line checks the number is high 
            print("Too High :",guess_num) #This line prints the number is two high if guessed value is high
        elif guess_num < Secret_num: #This line of code checks the number is low 
            print("Too Low :") #This line prints the numbe is low if guessd number is low
        else:
            print("conratulations!👍🥳 You Guessed the number") #if player wid this line will execute
            break #program will ends here if player guessed the number correctly
    else:
        print("sorry , You have no more attempts") #If not(guessed number is incorrect) it prints the sorry along with secret number
        print("Secret number is :",Secret_num)
def play_again(): #This function will get the input from palyer as yes or no then decide to paly again or quit.
    while True:
        choice = input("Do you want to play again? (yes/no): ")
        if choice.lower() == "yes":
            play_game()
        elif choice.lower() == "no":
            print("Thank you for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

# Start the game
play_game()

# Ask to play again
play_again()



