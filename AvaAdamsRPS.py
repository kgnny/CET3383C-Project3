'''
CET3383C-Project3
Software Engineering 1
 
Project 3: Rock, Paper, Scissors, Saw Game & Design Specifications Document
 
Due Date: October 22, 2023

Description:   This project simulates a game of Rock, Paper, Scissors, Saw.
                The game output will be used to complete Sections 3-5 of the SSD
'''
import random 
# Functions

# Prompts for player names, validates input, call menu()
def initialScreen():
  print("Rock, Paper, Scissors, Saw")
  print("---------------------------")

# Displays menu options and prompts for user input
def menu():
  print("Menu")
  print("---------------------------")

# "Back button" - Accepts input to return to the Menu
def validateReturnToMenu():
    print("Enter 1 to return to the Menu")
    userInput = input()
    if userInput == '1':
       print("\n")
       menu()
    else:
        print("Invalid input.")
        validateReturnToMenu()

'''
Rows: playerIndex, j
    0 - player1
    1 - player2
    2 - computer
Columns: statsIndex, i
    0 - rounds won
    1 - rounds lost
    2 - rounds tied
    3 - games won
    4 - games lost
    5 - games tied
'''
# Displays stats information
def stats(stats, player1_name, player2_name):
  print("Statistics")
  print("---------------------------")
  # print stats array
  for row in range(len(stats)):
        # print name of player
        if (row == 0):
            print(player1_name)
        elif (row == 1):
            print(player2_name)
        else:
            print("Computer")

        # print stats
        for column in range(len(stats[0])):
            if (column == 0):
                print("Rounds won:  ", stats[row][column]," ")
            elif (column == 1):
                print("Rounds lost: ", stats[row][column]," ")
            elif (column == 2):
                print("Rounds tied: ", stats[row][column]," ")
            elif (column == 3):
                print("Games won:   ", stats[row][column]," ")
            elif (column == 4):
                print("Games lost:  ", stats[row][column]," ")
            else:
                print("Games tied:  ", stats[row][column]," ")
        print("\n")

  validateReturnToMenu()

def createStatsArray():
    stats = [[0 for i in range(6)] for j in range(3)]  # all columns are initialized to 0 at the start of the game
    return stats

def updateStatsPlayer(stats, playerIndex, statsIndex):
    stats[playerIndex][statsIndex] = stats[playerIndex][statsIndex] + 1
    
# Displays rules for winning and basic instructions
def rules():
  print("Winner of the round will be determined as follow:")
  print("   a. Rock breaks scissors and Saw therefore rock wins over scissors and saw. Rock loses against paper.")
  print("   b. Scissors cut paper therefore scissors win over paper. Scissors lose against rock and Saw.")
  print("   c. Paper covers rock therefore paper wins over rock. Paper loses against scissors and saw")
  print("   d. Saw cuts through scissors and paper therefore saw wins over scissors and paper. Saw loses against rock.")
  print("   e. If player and computer make the same selection, there is a tie")
  print("")
  print("Winner of the game against the computer is one who won more rounds (must account for ties)")
  print("")
  print("Overall human winner is based on the greater number of won games against the computer and least games lost (must account for tie between human players)")
  print("")
  validateReturnToMenu()
 
statistics = createStatsArray()
# Play game, 3 rounds per game
def play(player1_name, player2_name):
    player1_name = "John" #placeholder
    player2_name = "James" #placeholder
    player1_winCount = 0
    player2_winCount = 0

    for round in range(1, 4):
        print(f"Round {round}:")
        
        # Generate a random selection for the computer
        computer_selection = random.randint(1, 4)
        
        player1_selection = get_player_selection(player1_name)
        player2_selection = get_player_selection(player2_name)

        print(f"{player1_name} chose {get_selection(player1_selection)}")
        print(f"{player2_name} chose {get_selection(player2_selection)}")
        print(f"Computer chose {get_selection(computer_selection)}")

        result1 = determine_winner(player1_name, player1_selection, computer_selection)
        result2 = determine_winner(player2_name, player2_selection, computer_selection)

        print(f"{player1_name} vs. Computer: {result1}")
        print(f"{player2_name} vs. Computer: {result2}\n")

        if result1 == f"{player1_name} wins!":
            player1_winCount += 1
            updateStatsPlayer(statistics, 0, 0)  # Player 1 wins round
            updateStatsPlayer(statistics, 2, 1)  # Computer loses
        elif result1 == "Computer wins":
            computer_winCount += 1
            updateStatsPlayer(statistics, 2, 0)  # Computer wins round
            updateStatsPlayer(statistics, 0, 1)  # Player 1 loses
        else:
            updateStatsPlayer(statistics, 0, 2) #tie
            updateStatsPlayer(statistics, 2, 2)

        if result2 == f"{player2_name} wins!":
            player2_winCount += 1
            updateStatsPlayer(statistics, 1, 0)  # Player 2 wins round
            updateStatsPlayer(statistics, 2, 1)  # Computer loses
        elif result2 == "Computer wins":
            computer_winCount += 1
            updateStatsPlayer(statistics, 2, 0)  # Computer wins round
            updateStatsPlayer(statistics, 1, 1)  # Player 2 loses
        else:
            updateStatsPlayer(statistics, 1, 2) #tie
            updateStatsPlayer(statistics, 2, 2)


    print("Winners of the game:")
    print("-------------------")
    print(f"{player1_name} vs Computer:")
    if player1_winCount > computer_winCount:
        print(f"{player1_name} wins the game!")
        updateStatsPlayer(statistics, 0, 3)  # Player 1 wins the game
        updateStatsPlayer(statistics, 2, 4)  # Computer loses the game
    elif player1_winCount == computer_winCount:
        print(f"{player1_name} tied against the computer!")
        updateStatsPlayer(statistics, 0, 5)  # Game tied for Player 1
        updateStatsPlayer(statistics, 2, 5)
    else:
        print("The computer wins the game!")
        updateStatsPlayer(statistics, 2, 3)  # Computer wins the game
        updateStatsPlayer(statistics, 0, 4)  # Player 1 loses the game

    print("-------------------")
    print(f"{player2_name} vs Computer:")
    if player2_winCount > computer_winCount:
        print(f"{player2_name} wins the game!")
        updateStatsPlayer(statistics, 1, 3)  # Player 2 wins the game
        updateStatsPlayer(statistics, 2, 4)  # Computer loses the game
    elif player2_winCount == computer_winCount:
        print(f"{player2_name} tied against the computer!")
        updateStatsPlayer(statistics, 1, 5)  # Game tied for Player 2
        updateStatsPlayer(statistics, 2, 5)
    else:
        print("The computer wins the game!")
        updateStatsPlayer(statistics, 2, 3)  # Computer wins the game
        updateStatsPlayer(statistics, 1, 4)

    print("Updating statistics...")
    stats(statistics, player1_name, player2_name)  # Display and store statistics

    validateReturnToMenu()

def get_player_selection(player_name):
    while True:
        print(f"{player_name}, please choose:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Saw")
        try:
            selection = int(input("Enter the number of your choice: "))
            if 1 <= selection <= 4:
                return selection
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
def get_selection(selection):
    if selection == 1:
        return "rock"
    elif selection == 2:
        return "paper"
    elif selection == 3:
        return "scissors"
    elif selection == 4:
        return "saw"

def determine_winner(playername, player_selection, computer_selection):
    if player_selection == computer_selection:
        return "It's a tie!"
    
    if (player_selection == 1 and (computer_selection == 3 or computer_selection == 4)) or \
       (player_selection == 2 and (computer_selection == 1)) or \
       (player_selection == 3 and (computer_selection == 2)) or \
       (player_selection == 4 and (computer_selection == 2 or computer_selection == 3)):
        return f"{playername} wins!"
    else:
        return "Computer wins"

def main():
  initialScreen()

# *** BEGINNING OF PROGRAM LOGIC***
# call main() method here
#main()

#play("John", "James") #test
#stats(createStatsArray(), "John", "James") #test
