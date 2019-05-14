# pylint: disable=C0301
# pylint: disable=C0111

import subprocess  # Used to call the urxvt terminal
import webcolors  # Used to get the closest color found by pywal, and launch urxxvt tinted with said color.

def main():
    """
    First, it grabs the hex color code outputted by pywal.
    Second, it calls upon the closest_colour function
    Finally, it calls the terminal process.
    """
    with open('/home/dersyx/.cache/wal/colors.Xresources') as file:  # Opens .Xresources file for grabbing the hex color code.
        colors = file.read().split()  # Splits the file by line and whitespace.
        if '*background:' in colors:
            index = colors.index('*background:')  # Finds the list index of the background value
            index = index + 1  # Adds one to index to get the background hex code.
            closest_name = closest_color(colors[index])  # Calls upon closest_color function.
            print(closest_name)
            if closest_name == 'black':  # makes sure that the black value doesn't remove the blur effect, which it does (probably a bug).
                subprocess.run('urxvt -tint gray', shell=True)  # Calls urxvt with gray tint to keep transparent blur.
            else:  # If the background value *isn't* black, runs following code.
                subprocess.run('urxvt -tint {}'.format(closest_name), shell=True)  # Calls urxvt with whatever color tint closest_olor finds.


def closest_color(requested_color):
    """
    Uses the webcolors module to find the closest color based on the hex code provided by pywal.
    Stolen from online.
    """
    requested_color = webcolors.hex_to_rgb(requested_color)  # Changes the hex code to rgb for better guessing
    min_colors = {}  # Provides a dictionary to output to.
    for key, name in webcolors.css21_hex_to_names.items():  # Outputs all possible hex to name colors provided by webcolors.
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)  # Changes key to rgb encoding.
        r_d = (r_c - requested_color[0]) ** 2  # Checks if the red value is closest to *name* color code.
        g_d = (g_c - requested_color[1]) ** 2  # Checks if the green value is closest to *name* color code.
        b_d = (b_c - requested_color[2]) ** 2  # Checks if the blue value is closest to *name* color code.
        min_colors[(r_d + g_d + b_d)] = name  # Sets the min_colors value to the name value.
    return min_colors[min(min_colors.keys())]  # Returns the guessed color name based off of the provided hex code.

main()  # Calls the main function
