import json

def initializeBoard():
    with open('scoreboard.json', 'r') as f:
        scoreboard = json.load(f)
    return scoreboard

def addplayer(name, scoreboard):
    scoreboard[name] = 0
    syncfile(scoreboard)
    return "Added player " + name

def deleteplayer(name, scoreboard):
    del scoreboard[name]
    syncfile(scoreboard)
    return "Deleted player " + name

def getscore(name, scoreboard):
    return name + ": " + str(scoreboard[name])

def addOne(name, scoreboard):
    scoreboard[name] += 1
    syncfile(scoreboard)
    return "Added point to " + name

def addpoints(name, points, scoreboard):
    scoreboard[name] += points
    syncfile(scoreboard)
    return "Added " + str(points) + " point(s) to " + name

def showplayers(scoreboard):
    retStr = ""
    for key, value in scoreboard.items():
        retStr += key + ": " + str(value) + "\n"

    return retStr

def syncfile(scoreboard):
    with open("scoreboard.json", 'w') as f:
        json.dump(scoreboard, f)

    return "Current scoreboard saved"

def help():
    retStr = "Here all of the commands you can use with botza:"
    retStr += "\n/addplayer [name]: will allow you to add a player to the scoreboard with the provided name"
    retStr += "\n/deleteplayer [name]: will allow you to delete the given player from the scoreboard"
    retStr += "\n/getscore [name]: will return the score of just that given player"
    retStr += "\n/addone [name]: allows you to add one point to the given players name"
    retStr += "\n/addpoints [points] [name]: will add the given points to the given players score"
    retStr += "\n/showplayers shows the entire scoreboard"
    retStr += "\n/syncfile: syncs the scripts data structure with a storage solution"
    retStr += "\n/help: provides a list of commands"
    retStr += "\n/johnxina: a mystery command"
    return retStr

def johnxina():
    return "早上好中国，这是冰淇淋。"

def reset(scoreboard):
    for key, value in scoreboard.items():
        scoreboard[key] = 0
    syncfile(scoreboard)
    return "Reset the scoreboard"

def setScore(name, score, scoreboard):
    scoreboard[name] = score
    syncfile(scoreboard)
    return "Gave " + name + " a score of " + str(score)