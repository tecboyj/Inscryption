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

if __name__ == "__main__":
    random_deck()

    load_gamestate()
    load_cards(player1deck["deck"], player2deck["deck"])
    save_gamestate()

    while(gameover == False):
        load_gamestate()
        draw()

        while(True):
            play = input("1) Play a card\n2) Ring Bell")
            if (play == "1"):
                card = input("Which card do you want to play? ")
                if (card == "1" or card == "2" or card == "3" or card == "4"):
                    if (playerdata["board"][card] == None):
                        card = playerdata["hand"].pop(int(card)-1)
                        playerdata["board"][card["position"]] = card
                    else:
                        print("There is already a card there!")
                else:
                    print("That is not a valid card!")
            else:
                break





        save_gamestate()
