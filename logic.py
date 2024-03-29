import json
from random import randint


player = None
players = {"1": "player1", "2": "player2"}
gamedata = None
playerdata = None
opponentBoard = None
gameover = False

cards= None

def load_gamestate(x):
    global player
    global gamedata
    global opponentBoard
    global playerdata

    with open("game.json", 'r') as file:
        data = json.load(file)
        player = str(data["turn"])
        gamedata = data
        playerdata = data[players[player]]
        opponentBoard = data[players[str(2 if player == "1" else 1)]]["board"]

    global cards
    with open("cards.json", 'r') as file:
        cards = json.load(file)

def load_cards(player1deck, player2deck):
    global gamedata
    global playerdata

    gamedata["player1"]["deck"] = player1deck
    gamedata["player2"]["deck"] = player2deck
    playerdata["deck"] = gamedata[players[player]]["deck"]

def save_gamestate():
    global gamedata

    gamedata["turn"] = 2 if player == "1" else 1
    with open("game.json", 'w') as file:
        json.dump(gamedata, file)

def draw(x):
    global playerdata
    global cards

    if (playerdata["hand"] == []):
        for i in range(3):
            playerdata["hand"].append(cards["squirl"])
            playerdata["hand"].append(playerdata["deck"].pop(randint(0, len(playerdata["deck"])-1)))
    else:
        if (playerdata["deck"] == []):
            if (playerdata["squirls"] == 0):
                print("You have no cards left to draw!")
                return
            else:
                draw_squirl()
        elif (playerdata["squirls"] == 0):
            draw_deck()
        else:
            if (x == "1"):
                draw_squirl()
            else:
                draw_deck()
def draw_squirl():
    playerdata["hand"].append(cards["squirl"])
    playerdata["squirls"] -= 1
def draw_deck():
    playerdata["hand"].append(playerdata["deck"].pop(randint(0, len(playerdata["deck"])-1)))

def attack():
    for i in range(4):
        attack_loop(str(i + 1))


def attack_loop(place):
    global playerdata
    global opponentBoard
    global gamedata
    global player

    if ((opponentBoard[place] != None) and (playerdata["board"][place] != None)):
        print("1) " + opponentBoard["1"]["name"])
    elif ((opponentBoard[place] == None) and (playerdata["board"][place] != None)):
        match player:
            case 1: gamedata["score"] += playerdata["board"][place]["attack"]
            case 2: gamedata["score"] -= playerdata["board"][place]["attack"]


def score():
    global gamedata
    global gameover

    if (gamedata["score"] > 4):
        print("Player 1 wins!")
        gameover = True
    elif (gamedata["score"] < -4):
        print("Player 2 wins!")
        gameover = True
