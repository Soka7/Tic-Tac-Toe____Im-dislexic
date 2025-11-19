from GameData import Actions

def CheckWinner(action1 : str, action2 : str):

    assert type(action1) == str, "The first action must be a string."
    assert type(action2) == str, "The second action must be a string."

    IsValid : bool = False
    for key in Actions.keys():
        if key == action1:
            IsValid = True

    assert IsValid, "First action is not a possible action !"

    IsValid = False

    for key in Actions.keys():
        if key == action2:
            IsValid = True

    assert IsValid, "Second Action is not a possible action !"

    if action1 == action2:
        return "T: Tie !"
    
    for advantages in Actions[action1]["Win"]:
        if action2 == advantages:
            return "1: Won !"
    for weaknesses in Actions[action1]["Lose"]:
        if action2 == weaknesses:
            return "2: Won !"
        
    return -1