import microbit
import radio

radio.config(address=TicTacToeMore, group=0, channel=83) 
# adress is to only use the microbit with falshed code
# we'll use 2 group : 255 (Referee to Player) and 0 (Player To Referee)
# channel 83 will be the Regeree channel, and Player have they own radio from 0 to 82 (like we getting 82 microbit)

while True:
    