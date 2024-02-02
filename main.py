from random import randint
from logic import *

player1deck = {"deck": []}
player2deck = {"deck": []}

def random_deck():
    with open("cards.json", "r") as file:
        cards = json.load(file)
    
    global player1deck
    global player2deck

    player1deck["deck"].append(cards["stoat"])
    for i in range(6):
        player1deck["deck"].append(cards["common"][randint(0, 3)])
    player1deck["deck"].append(cards["rare"][randint(0, 1)])

    player2deck["deck"].append(cards["stoat"])
    for i in range(6):
        player2deck["deck"].append(cards["common"][randint(0, 3)])
    player2deck["deck"].append(cards["rare"][randint(0, 1)])

def reset():
    game = {"turn": 1, "player1": {"board": {"1": None, "2": None, "3": None, "4": None}, "hand": [], "deck": [], "squirls": 6}, 
            "player2": {"board": {"1": None, "2": None, "3": None, "4": None}, "hand": [], "deck": [], "squirls": 6}}
    with open("game.json", 'w') as file:
        json.dump(game, file)

def print_board():
    global playerdata
    global opponentBoard

    opponent = []
    player = []

    for i in range(4):
        if (opponentBoard[str(i + 1)] != None):
            opponent.append(opponentBoard[str(i + 1)])
        else:
            opponent.append("")
        if (playerdata["board"][str(i + 1)] != None):
            player.append(playerdata["board"][str(i + 1)])
        else:
            player.append("")
        
        if (len(player[i]) > len(opponent[i])):
            x = len(player[i]) - len(opponent[i])
            for j in range(x):
                opponent[i] += " "
        elif (len(opponent[i]) > len(player[i])):
            x = len(opponent[i]) - len(player[i])
            for j in range(x):
                player[i] += " "
        else:
            for j in range(2):
                opponent[i] += " "
                player[i] += " "

    print(opponent[1] + "|" + opponent[2] + "|" + opponent[3] + "|" + opponent[4])
    print("----------------------------------------------------------------------------")
    print(player[1] + "|" + player[2] + "|" + player[3] + "|" + player[4])

if __name__ == "__main__":
    random_deck()

    load_gamestate()
    load_cards(player1deck["deck"], player2deck["deck"])
    save_gamestate()

    while(gameover == False):
        load_gamestate()
        draw(input("1) Squirl\n2) Draw\n"))

        while(True):
            play = input("1) Play a card\n2) Ring Bell\n")
            if (play == "1"):
                card = int(input("Which card do you want to play?\n"))
                if (card < len(playerdata["hand"])):
                    card = playerdata["hand"].pop(card - 1)
                    occupied = 0
                    for i in range(4):
                        if (playerdata["board"][str(i + 1)] != None):
                            occupied += 1
                    if (card["cost"] < occupied):
                        for i in range(len(card["cost"])):
                            playerdata["board"][input("Select a card to sacrifice\n")] = None
                            print_board()
                        boardpos = input("Where do you want to play it?\n")
                        if (playerdata["board"][boardpos] == None):
                            playerdata["board"][boardpos] = card
                        else:
                            print("There is already a card there!")
                    else:
                        print("You do not have enough blood to play that card!")
                else:
                    print("That is not a valid card!")
            else:
                break




        score()
        save_gamestate()
    reset()