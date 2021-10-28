# Programmer: Peter Hope
# Class: CS 151-02
# Date: 10/27/2021
# Programming Assignment 3
# Inputs: desired statistic choice, and the corresponding inputs for each choice
#       Football Inputs: completions, passing_yards, touchdown_passes, interceptions, and attempts
#       Quidditch Inputs: number of goals, is snitch caught
#       Gymnast Inputs: difficulty, 5 execution scores
# Outputs: stat of chosen sport (quarter back rating, quidditch score, or gymnast final score

# calculates the Quarterback Rating of a player with the stats user enters
def f_score():
    print ("This will calculate the Quarterback Rating of a player with the stats you enter")
    # asks for the number of attempts input
    attempts = input("input the number of attempts: ")
    # tests if the input is all digits and will stop the program if it isn't
    if (attempts.isdigit() == False):
        print("Error: can only be float or int")
        return 0
    else:
        # if it is all digits, it will convert the input to float, repeat these test and conversion steps for the following inputs
        attempts = float(attempts)
    # tests the input for attempts is not 0
    if (attempts == 0):
        print("Error: attempts cannot be 0")
        return 0
    # asks the user for the number of completions
    completions = input("input the number of completions: ")
    if (completions.isdigit() == False):
        print("Error: can only be float or int")
        return 0
    else:
        completions = float(completions)
    # asks the user for the number of passing yards
    passing_yards = input("input the number of passing yards: ")
    if (passing_yards.isdigit() == False):
        print("Error: can only be float or int")
        return 0
    else:
        passing_yards = float(passing_yards)
    # asks the user for the number of passing touchdowns
    touchdown_passes = input("input the number of touchdown passes: ")
    if (touchdown_passes.isdigit() == False):
        print("Error: can only be float or int")
        return 0
    else:
        touchdown_passes = float(touchdown_passes)
    # asks the user for the number of interceptions
    interceptions = input("input the number of interceptions: ")
    if (interceptions.isdigit() == False):
        print("Error: can only be float or int")
        return 0
    else:
        interceptions = float(interceptions)
    # as I was writing this code I realized that the given formula was not matching up with examples I had found online for real-life quarter back ratings so I added an option to use the formula used in real life so that you would get an accurate rating
    form = input ("would you like to use the formula given in the directions (type x) or the official formula (type y) ")
    # calculates the quarter back rating using the given formula
    if (form == "x"):
        c = (completions/attempts - 0.3) * 5
        p = (passing_yards/attempts-3) * 0.25
        t = (touchdown_passes/attempts) * 20
        i = 2.375 - ((interceptions/attempts) * 25)
        a = c + p + t + i
        qbr = (a/6) * 100
    # calculates the quarter back rating using the other formula
    else:
        c = (completions / attempts - 0.3) * 5
        if (c > 2.375):
             c=2.375
        p = (passing_yards / attempts - 3) * 0.25
        if (p > 2.375):
            p=2.375
        t = (touchdown_passes / attempts) * 20
        if (t > 2.375):
            t=2.375
        i = 2.375 - ((interceptions / attempts) * 25)
        a = c + p + t + i
        qbr = (a/6) * 100
    # rounds the quarter back rating to 1 decimal point
    qbr = round (qbr, 1)
    # prints a statement if the calculated quarter back rating is considered a perfect rating of 158.3
    if (qbr == 158.3):
        print ("Perfect Passer Rating!")
    # prints the quarter back rating
    print(qbr)

# calculates the score for a team in Quidditch
def q_score():
    print ("This will calculate the score for a Quidditch team based off the stats you enter")
    # asks for the number of goals scored to be inputted
    goals = input("input the number of goals scored: ")
    # makes sure that the input is only digits and if it isn't, it shows the error
    if (goals.isdigit() == False):
        print("Error: can only be float or int")
        return 0
    else:
        # if it is all digits it converts the input to a float
        goals = float(goals)
    # asks the user if the team caught the snitch
    snitch = (input("did the team catch the snitch? (yes or no) "))
    # if the user answers yes it will calculate the team's score with the additional points from the snitch
    if (snitch=="yes"):
        points = goals*10 + 30
    # if the user answers no it will calculate the team's score without the additional points from the snitch
    else:
        points = goals*10
    # prints the teams final score
    print (points)

# calculates a gymnast's final score on any apparatus
def g_score():
    print ("This will calculate the score for a gymnasts routine based of the scores you enter")
    # asks the user for the difficulty score
    diff = input("difficulty score: ")
    # tests that the inputted score is all digits, if it isn't it will show the error
    if (diff.isdigit() == False):
        print("Error: can only be float or int")
        return 0
    else:
        # if it is all digits it will convert the input to a float, these test and conversion steps are repeated for the following inputted scores
        diff = float(diff)
    # asks for first execution score
    ex1 = input("execution score 1: ")
    if (ex1.isdigit() == False):
        print("Error: can only be float or int")
        return 0
    else:
        ex1 = float(ex1)
    # asks for second executions score
    ex2 = input("execution score 2: ")
    if (ex2.isdigit() == False):
        print("Error: can only be float or int")
        return 0
    else:
        ex2 = float(ex2)
    # asks for third executions score
    ex3 = input("execution score 3: ")
    if (ex3.isdigit() == False):
        print("Error: can only be float or int")
        return 0
    else:
        ex3 = float(ex3)
    # asks for forth executions score
    ex4 = input("execution score 4: ")
    if (ex4.isdigit() == False):
        print("Error: can only be float or int")
        return 0
    else:
        ex4 = float(ex4)
    # asks for fifth executions score
    ex5 = input("execution score 5: ")
    if (ex5.isdigit() == False):
        print("Error: can only be float or int")
        return 0
    else:
        ex5 = float(ex5)
    # calculates the gymnast's final score
    final = diff + ((ex1+ex2+ex3+ex4+ex5)/5)
    # prints teh gymnast's final score
    print ("Final Score = ", final)

# main function that calls the other functions
def main ():
    # asks which sport the user would like the statistic to be about
    print ("Which sport would you like the statistic to be about?")
    choice = input ("Football, Quidditch, or Gymnastics ")
    # changes the input to all lower case with no spaces in the front or back
    choice = choice.lower().strip()
    # if the user chooses football, the f_score function will run
    if (choice == "football"):
        stat = f_score()
    # if the user chooses quidditch, the q_score function will run
    elif (choice == "quidditch"):
        stat = q_score()
    # if the user chooses gymnastics, the g_score function will run
    elif (choice == "gymnastics"):
        stat = g_score()
    # if the user does not properly input football, quidditch, or gymnastics, it will show the error
    else:
        print ("Input a valid sport choice")
main ()

