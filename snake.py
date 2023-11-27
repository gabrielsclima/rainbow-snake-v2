# Libraries
from time import sleep
from keyboard import is_pressed
is_pressed('left') # Just to avoid a delay being caused by this function. Don't worry, it's temporary.

# Colors
red = "\033[0;31m"
cyan = "\033[0;36m"
green = "\033[0;32m"
yellow = "\033[1;33m"
purple = "\033[0;35m"
end_color = "\033[0m"

# Rainbow Settings
color_sequence = [red, yellow, green, cyan, purple]
rainbow_size = 5
min_position = 0
max_position = 0
while max_position <= 0:
    try:
        max_position = int(input("Declare the maximum position for the snake: "))
        if max_position <= 0:
            print("How do you expect to see the snake moving?")
            print("Do not declare something below or equal to zero")
        else:
            current_position = max_position // 2
    except ValueError:
        print("Sorry, use numbers only.")

# Movement
def makeRow():
    print(" " * current_position, end="")
    for i in range(rainbow_size):
        #square = color_sequence[(current_position + i) % 5] + "█" * 2
        square = color_sequence[(current_position + i) % 5] + f"{(current_position + i) % 5}" * 2
        print(square, end="")
    print(end_color)
    sleep(0.02)

def makeRowStop():
    print(" " * current_position, end="")
    square = color_sequence[(current_position)]
    print()
    for i in range(rainbow_size - 2):
        square = color_sequence[(current_position + i) % 5] + f"{(current_position + i) % 5}" * 2
        #square = color_sequence[(current_position + i) % 5] + "█" * 2
        print(square, end="")
    print(end_color)
    sleep(0.02)
    
def checkKeyPressed():
    global current_position
    while is_pressed('left') and current_position > min_position:
        current_position -= 1
        makeRow()

    while is_pressed('right') and current_position < max_position:
        current_position += 1
        makeRow()

# Get ready for fun!
while True:
    makeRow()
    checkKeyPressed()
