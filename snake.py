# Libraries
from time import sleep
from keyboard import is_pressed

# Colors
red = "\033[0;31m█" 
cyan = "\033[0;36m█"
green = "\033[0;32m█"
yellow = "\033[1;33m█"
purple = "\033[0;35m█"
end_color = "\033[0m"

# Rainbow settings
color_sequence = [red, yellow, green, cyan, purple]
rainbow_size = 5
minimum_position = 0
maximum_position = 0
current_position = maximum_position // 2

while maximum_position == 0:
    try:
        maximum_position = int(input("Declare the maximum position for the snake: "))
    except ValueError:
        print("Hmm... I think that is not an intenger number. Try it again.")

# Get ready for fun!
while True:
    print(" " * current_position, end="")

    for i in range(rainbow_size):
        print(color_sequence[(current_position + i) % 5], end="")
        print(color_sequence[(current_position + i) % 5], end="")
    
    if is_pressed('left') and current_position > minimum_position:
            current_position -= 1

    elif is_pressed('right') and current_position < maximum_position:
            current_position += 1

    print(end_color)
    sleep(0.02)
