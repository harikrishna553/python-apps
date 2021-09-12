import random

def guess_number(min_value, max_value, no_of_attempts):
    number_to_Guess = random.randint(min_value, max_value)

    guess = False
    count = no_of_attempts

    while guess == False:
        my_guess = input("Enter a number between " + str(min_value) + " and " + str(max_value) + "\n")
        my_guess = int(my_guess)

        if(my_guess == number_to_Guess):
            print("Hurray!!! you won")
            guess = True
        elif(my_guess > number_to_Guess):
            print("Your guess is greater than actual number")
        else:
            print("Your guess is less than actual number")

        count -= 1

        if(count == 0):
            print("Total attempts finished")
            break
        print("remaining attempts : ", count)

guess_number(10, 20, 5)