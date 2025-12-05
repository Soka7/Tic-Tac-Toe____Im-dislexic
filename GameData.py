from microbit import *

# Dictionarry used to store each actions, with its name and shape displayed.
# Shape is stored as an Image object of the microbit module.
# It also contains the weaknesse and advantages of each action.

Actions : dict = {
    "Rock_" : {
        "Shape" : Image("00000:"
                        "09990:"
                        "09990:"
                        "09990:"
                        "00000"),
        "Name" : "Rock_",
        "Win" : ["Lizar", "Sciss"],
        "Lose" : ["Paper", "Spock"],
    },
    "Paper" : {
        "Shape" : Image("00000:"
                        "99999:"
                        "99999:"
                        "99999:"
                        "00000"),
        "Name" : "Paper",
        "Win" : ["Rock_", "Spock"],
        "Lose" : ["Sciss", "Lizard"],
    },
    "Sciss" : {
        "Shape" : Image("99009:"
                        "99090:"
                        "00900:"
                        "99090:"
                        "99009"),
        "Name" : "Sciss",
        "Win" : ["Paper", "Lizard"],
        "Lose" : ["Spock", "Rock_"],
    },
    "Lizar" : {
        "Shape" : Image("00900:"
                        "99099:"
                        "09090:"
                        "99099:"
                        "00900"),
        "Name" : "Lizar",
        "Win" : ["Paper", "Spock"],
        "Lose" : ["Sciss", "Rock_"],
    },
    "Spock" : {
        "Shape" : Image("00999:"
                        "09999:"
                        "99900:"
                        "09999:"
                        "00999"),
        "Name" : "Spock",
        "Win" : ["Rock_", "Sciss"],
        "Lose" : ["Paper", "Lizar"],
    },
}

Matching = {
    0:"Lizar",
    1:"Spock",
    2:"Sciss",
    3:"Paper",
    4:"Rock_"
}
