# Libraries
from time import sleep
import keyboard

# Colors
red = "\033[0;31m█" 
cyan = "\033[0;36m█"
green = "\033[0;32m█"
yellow = "\033[1;33m█"
purple = "\033[0;35m█"
end_color = "\033[0m"

# Rainbow settings
color_sequence = [red, yellow, green, cyan, purple]
rainbow_width = 5
minimum_position = 0
maximum_position = 0

while maximum_position == 0:
    try:
        maximum_position = int(input("Declare the maximum position for the snake: "))
        current_position = maximum_position // 2
    except ValueError:
        print("Hmm... I think that is not an intenger number. Try it again.")

# Get ready!
while True:
    print(" " * current_position, end="")

    for width_position in range(rainbow_width):
       print(color_sequence[(current_position + width_position) % 5], end="")
       print(color_sequence[(current_position + width_position) % 5], end="")
    
    # TODO: Find a way to not need 2 if statements, but keep the code as clean as possible.
    # Using elif has a bit of an issue:
    # It won't "understand" that if you press left and right, you don't want the snake to move.
    if keyboard.is_pressed('left') and current_position > minimum_position:
        current_position -= 1

    if keyboard.is_pressed('right') and current_position < maximum_position:
        current_position += 1

    print(end_color)
    sleep(0.02)
