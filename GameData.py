from microbit import *

# Dictionarry used to store each actions, with its name and shape displayed.
# Shape is stored as an Image object of the microbit module.
# It also contains the weaknesse and advantages of each action.

Actions : dict = {
    "Rock" : {
        "Shape" : Image("00000:"
                        "09990:"
                        "09990:"
                        "09990:"
                        "00000"),
        "Name" : "Rock",
        "Win" : ["Lizard", "Scissors"],
        "Lose" : ["Paper", "Spock"],
    },
    "Paper" : {
        "Shape" : Image("00000:"
                        "99999:"
                        "99999:"
                        "99999:"
                        "00000"),
        "Name" : "Paper",
        "Win" : ["Rock", "Spock"],
        "Lose" : ["Scissors", "Lizard"],
    },
    "Scissors" : {
        "Shape" : Image("99009:"
                        "99090:"
                        "00900:"
                        "99090:"
                        "99009"),
        "Name" : "Scissors",
        "Win" : ["Paper", "Lizard"],
        "Lose" : ["Spock", "Rock"],
    },
    "Lizard" : {
        "Shape" : Image("00900:"
                        "99099:"
                        "09090:"
                        "99099:"
                        "00900"),
        "Name" : "Lizard",
        "Win" : ["Paper", "Spock"],
        "Lose" : ["Scissors", "Rock"],
    },
    "Spock" : {
        "Shape" : Image("00999:"
                        "09999:"
                        "99900:"
                        "09999:"
                        "00999"),
        "Name" : "Spock",
        "Win" : ["Rock", "Scissors"],
        "Lose" : ["Paper", "Lizard"],
    },
}

Matching = {
    0:"Lizard",
    1:"Spock",
    2:"Scissors",
    3:"Paper",
    4:"Rock"
}
