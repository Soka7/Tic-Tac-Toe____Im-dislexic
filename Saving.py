def SavingParty(TheStuffUWannaWrite):
    with open("PartySaves.txt", "a") as File:
        File.write(f"Save:{TheStuffUWannaWrite}\n")
        
def Clean():
    with open("PartySaves.txt", "w") as File:
        File.write("")