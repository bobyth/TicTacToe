
# Display the game board with 9 position for X and Y
# Make sure the board is empty
# Provide numbers for each cell so the players can refer to it.
# Provide error message for placing a symbol in a filled cell
# if player has 3 symbols in a line, display "You Win" message.

theBoard = {"7": "", "8": "", "9": "",
            "4": "", "5": "", "6": "",
            "1": "", "2": "", "3": ""}
BoardKeys = []

for key in theBoard:
    BoardKeys.append(key)

def printBoard(board):
    print(board["7"] + " /" + board["8"] + " /" + board["9"])
    print("-+-+-")

    print(board["4"] + " /" + board["5"] + " /" + board["6"])
    print("-+-+-")

    print(board["1"] + " /" + board["2"] + " /" + board["3"])
    print("-+-+-")

def game():
    turn = "X"
    count = 0

    for i in range(10):

        printBoard(theBoard)
        print("it is turn of " + turn + " specify the place you want to go")

        move = input()

        if theBoard[move] == "":
            theBoard[move] = turn
            count += 1
        else:
            print("Sorry this cell location is filled. Please Choose an other one.")

            continue

        if count >= 5:

            if theBoard["7"] == theBoard["8"] == theBoard ["9"] != "":

                printBoard(theBoard)
                print("/nGame Over/n")
                print("Player " + turn + "won the game")

                break

            if theBoard["1"] == theBoard["2"] == theBoard ["3"] != "":

                printBoard(theBoard)
                print("/nGame Over/n")
                print("Player " + turn + "won the game")

                break

            if theBoard["1"] == theBoard["4"] == theBoard ["7"] != "":

                printBoard(theBoard)
                print("/nGame Over/n")
                print("Player " + turn + "won the game")

                break

            if theBoard["3"] == theBoard["6"] == theBoard ["9"] != "":

                printBoard(theBoard)
                print("/nGame Over/n")
                print("Player " + turn + "won the game")

                break

            if theBoard["1"] == theBoard["5"] == theBoard ["9"] != "":

                printBoard(theBoard)
                print("/nGame Over/n")
                print("Player " + turn + "won the game")

                break

            if theBoard["3"] == theBoard["5"] == theBoard ["7"] != "":

                printBoard(theBoard)
                print("\nGame Over\n")
                print("Player " + turn + "won the game")

                break

        if count == 9:
            print("\nGame Over\n")
            print("The game is Tie!")

        if turn == "X ":
            turn = "0 "

        else:
            turn = "X"

    restart = input("Do you want to restart the Game? (y/n)")

    if restart == "y" or restart == "Y":
        for key in BoardKeys:
            theBoard[key] = ""
            game()


if __name__ == "__main__":
    game()