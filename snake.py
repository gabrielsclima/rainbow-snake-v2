#Libraries
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
RB = (R, Y, G, C, P) #Rainbow
SNAKE_SIZE = 5
POS_MIN = 0 #Minimum position value
POS_MAX = int(input("How much the snake can slide on your screen: ")) #Maximum position value
currentPos = POS_MAX // 2 #Makes the snake start in the middle of the terminal, according to the POS_MAX declared by the user

while True:
    for i in range(5):
        if is_pressed('left') and currentPos > POS_MIN:
                currentPos -= 1
        elif is_pressed('right') and currentPos < POS_MAX:
             currentPos += 1
        print(" " * currentPos, end="")
        for j in range(SNAKE_SIZE): #
            print(RB[(currentPos + j) % 5], end="")
            print(RB[(currentPos + j) % 5], end="")
        print(END)
        sleep(0.02)
