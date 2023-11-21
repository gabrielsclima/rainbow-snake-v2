# Libraries
from time import sleep
from keyboard import is_pressed

# Colors
R = "\033[0;31m█" #Red
Y = "\033[1;33m█" #Yellow
G = "\033[0;32m█" #Green
C = "\033[0;36m█" #Cyan
P = "\033[0;35m█" #Purple
END = "\033[0m"   #End of color

# Rainbow settings
RB = (R, Y, G, C, P) # Rainbow colors.
SNAKE_SIZE = 5 # Snake... size.
POS_MIN = 0 # Minimum position value.
POS_MAX = int(input("How much the snake can slide on your screen: ")) # Maximum position value. 

# Obs: "Position" stands for the number of space characters 
# that will be printed before the rainbow row.
currentPos = POS_MAX // 2

# Get ready for fun!
while True:
    if is_pressed('left') and currentPos > POS_MIN:
            currentPos -= 1
    elif is_pressed('right') and currentPos < POS_MAX:
            currentPos += 1
    print(" " * currentPos, end="")

    for i in range(SNAKE_SIZE): #
        print(RB[(currentPos + j) % 5], end="")
        print(RB[(currentPos + j) % 5], end="")

    print(END)
    sleep(0.02)
