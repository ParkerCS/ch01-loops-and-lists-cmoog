import random
#LISTS (35PTS TOTAL)
#In these exercises you write functions. Of course, you should not only write the functions,
#you should also write code to test them. For practice, you should also comment your
#functions as explained above.

#PROBLEM 1 (8-ball - 5pts)
# A magic 8-ball, when asked a question, provides a random answer from a list.
# The code below contains a list of possible answers. Create a magic 8-ball program that
# prints a random answer.
answer_list = [ "It is certain", "It is decidedly so", "Without a \
doubt", "Yes, definitely", "You may rely on it", "As I see it, \
yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
"Reply hazy try again", "Ask again later", "Better not tell you \
now", "Cannot predict now", "Concentrate and ask again", "Don ' t \
count on it", "My reply is no", "My sources say no", "Outlook \
not so good", "Very doubtful" ]

def eight_ball(possible_answers):
    return(possible_answers[random.randrange(len(possible_answers))])
print(eight_ball(answer_list))


# PROBLEM 2 (Shuffle - 5pts)
# A playing card consists of a suit (Heart, Diamond, Club, Spade) and a value (2,3,4,5,6,7,8,9,10,J,Q,K,A).
# Create a list of all possible playing cards, which is a deck.
# Then create a function that shuffles the deck, producing a random order.
deck = []
cards = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
suits = ["C","H","S","D"]
for suit in suits:
    for card in cards:
        deck.append([card,suit])

def shuffle_deck(list):
    random.shuffle(list)
    return(list)
print(shuffle_deck(deck))


# PROBLEM 3 (The sieve of Eratosthenes - 10pts)
# The sieve of Eratosthenes is a method to find all prime numbers between
# 1 and a given number using a list. This works as follows: Fill the list with the sequence of
# numbers from 1 to the highest number. Set the value of 1 to zero, as 1 is not prime.
# Now loop over the list. Find the next number on the list that is not zero,
# which, at the start, is the number 2. Now set all multiples of this number to zero.
# Then find the next number on the list that is not zero, which is 3.
# Set all multiples of this number to zero. Then the next number, which is 5
# (because 4 has already been set to zero), and do the same thing again.
# Process all the numbers of the list in this way. When you have finished,
# the only numbers left on the list are primes.
# Use this method to determine all the primes between 1 and 1000.

sequence = []
def populate_sequence(max):
    for i in range(max):
        sequence.append(i)
def delete_zeros(list):
    done = False
    while not done:
        if list.count(0) != 0:
            list.remove(0)
        else:
            done = True

def eratosthenes_method(upper_limit):
    max = upper_limit + 100
    populate_sequence(max)
    for sequence_item in range(2, len(sequence)):
        if sequence[sequence_item] != 0:  # is it has already been turned to 0
            for multiple in range(2, max // sequence[sequence_item]): # the range is how many times you can multiply the number without going out of range
                sequence[multiple * sequence_item] = 0

    sequence[1] = 0
    delete_zeros(sequence)

    while sequence[len(sequence)-1] > upper_limit:
        sequence.pop()

    print(sequence)
    print(len(sequence))

eratosthenes_method(1000)

# PROBLEM 4 (Tic-Tac-Toe - 15pts)
# Write a Tic-Tac-Toe program that allows two people to play the game against each other.
# In turn, ask each player which row and column they want to play.
# Make sure that the program checks if that row/column combination is empty.
# When a player has won, end the game.
# When the whole board is full and there is no winner, announce a draw.
# This is a fairly long program to write (60 lines or so).
# It will definitely help to use some functions.
# I recommend that you create a function display_board() that gets the board
# as parameter and displays it,
# a function get_row_column() that asks for a row or a column (depending on a parameter)
# and checks whether the user entered a legal value,
# and a function winner() that gets the board as argument and checks if there is a winner.
# Keep track of who the current player is using a global variable player that you can
# pass to a function as an argument if the function needs it.
# I also use a function opponent(), that takes the player as argument and returns
# the opponent. I use that to switch players after each move.

# The main program will be something along the lines of (in pseudo-code):
# display board
# while True:
#   ask for row
#   ask for column
#       if row/column already occupied:
#           display error
#   place player marker in row/col
#   display board
#   check for winner:
#       announce winner
#       break
#   check board full:
#       announce draw
#       break
#   switch player

# 0 = empty
# 1 = x
# 2 = o
board = [
[0,0,0],
[0,0,0],
[0,0,0]
]
def display_board(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                print("x ", end="")
            elif board[row][col] == 2:
                print("o ", end="")
            else:
                print("- ", end="")
        print()
def get_row_column(board, player):
    error = False
    row = int(input("Please enter the row (1,2,3): ")) - 1
    col = int(input("Please enter the column (3,2,1): ")) - 1
    if board[row][col] != 0:
        print("Error: That space is taken.")
        error = True
    elif player == "x":
        board[row][col] = 1
    elif player == "o":
        board[row][col] = 2
    return board, error
def check_draw(board):
    if board[0].count(0) == 0 and board[1].count(0) == 0 and board[2].count(0) == 0:
        print("It's a draw. The game is over.")
        return "draw"
    else:
        return None
def product(list):
    result = 1
    for i in range(len(list)):
        result *= list[i]
    return result
def check_winner(board):
    for row in range(3): ## if there are three in a row
        if sum(board[row]) == 6:
            return "o"
        elif sum(board[row]) == 3 and product(board[row]):
            return "x"
    for col in range(3):
        if board[0][col] + board[1][col] + board[2][col] == 6:
            return "o"
        elif board[0][col] + board[1][col] + board[2][col] == 3 and board[0][col] * board[1][col] * board[2][col] == 1:
            return "x"
    if board[0][0] + board[1][1] + board[2][2] == 6:
        return"o"
    elif board[0][0] + board[1][1] + board[2][2] == 3 and board[0][0] * board[1][1] * board[2][2] == 1:
        return "x"
    if board[0][2] + board[1][1] + board[2][0] == 6:
        return "o"
    if board[0][2] + board[1][1] + board[2][0] == 3 and board[0][2] * board[1][1] * board[2][0] == 1:
        return "x"
game_over = False
player = "x"
while not game_over:
    board_and_value = get_row_column(board, player)  # to see if its a repeat and then don't swtich player
    board = board_and_value[0]
    error = board_and_value[1]
    display_board(board)
    if check_winner(board) == "o":
        game_over = True
        print("o has won the game")
    elif check_winner(board) == "x":
        game_over = True
        print("x has won the game")
    if check_draw(board) ==  "draw":
        game_over = True
    if player == "x" and not error:
        player = "o"
    elif not error:
        player = "x"
    print()

# CHALLENGE PROBLEM 5 (Battleship NO CREDIT, JUST IF YOU WANT TO TRY IT)
# Create a program that is a simplified version of the game “Battleship.”
# The computer creates (in memory) a grid that is 4 cells wide and 3 cells high.
# The rows of the grid are numbered 1 to 3, and the columns of the grid are labeled A to D.
# The computer hides a battleship in three random cells in the grid.
# Each battleship occupies exactly one cell.
# Battleships are not allowed to touch each other horizontally or vertically.
# Make sure that the program places the battleships randomly, so not pre-configured.
# The computer asks the player to “shoot” at cells of the grid.
# The player does so by entering the column letter and row number of the cell
# which she wants to shoot at (e.g., "D3").
# If the cell which the player shoots at contains nothing, the computer responds with “Miss!”
#  If the cell contains a battleship, the computer responds with “You sunk my battleship!”
# and removes the battleship from the cell (i.e., a second shot at the same cell is a miss).
# As soon as the player hits the last battleship, the computer responds with displaying
# how many shots the player needed to shoot down all three battleships, and the program ends.
# To help with debugging the game, at the start the computer should display the grid with
# O's marking empty cells and X's marking cells with battleships.
# Hint: If you have troubles with this exercise, start by using a board which has the
# battleships already placed.
# Once the rest of the code works, add a function that places the battleships at random,
# at first without checking if they are touching one another.
# Once that works, add code that disallows battleships touching each other.
