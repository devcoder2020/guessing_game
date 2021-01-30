# Lee Haynes
# Phone: + 44 (0) 785 374 0636
# Email: LeeHaynes2019@yandex.com
# Website: http://www.devcoder.me.uk/
# Instagram: junior_web_developer_2020
# Devcoder Youtube: https://www.youtube.com/channel/UCXqnASrfdoRlyt82YR7n7pQ?view_as=subscriber
# Lee Haynes Youtube: https://www.youtube.com/channel/UCjqLeiVDygmpCHXyeDzH04g

# Welcome to my guessing game

# create a data file
import random
file = open("results.txt", "a")

# import modules

# setting a strating and ending number
strating_range = 1
endoing_range = 50

# Using the randm module to select a number at random
reuslt = random.randint(strating_range, endoing_range)

# Setting the place holder variables
user_guess = "-"
count = 1


#percentage = (count / user_guess * 100)
# Ask user for name
name = input("Please enter your name: ")
print("Testing Purpose", reuslt)

# Setting the loop option
# untill the guess match then the user has to keep guessing
while user_guess != reuslt:
    user_guess = int(input("Please guess a number between 0 and 50: "))
    if user_guess > reuslt:
        print("Guess lower")
        count = count + 1
    elif user_guess < reuslt:
        print("Guess higher")
        count = count + 1
    else:
        print("Congrats you guessed correctly")

        # working out the guess percentage
        percentage = (count / user_guess)
        # print("The toal number of guess was: ",
        #       count, "Percentage: ", percentage, "guessing accuracy:")

        file.write(
            f"\nCongratulations: {name} it took {count} attempts to guess correctly and your percentage was: {percentage}")
        file.close()
