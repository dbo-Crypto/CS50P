from pyfiglet import Figlet
import random
import sys


figlet = Figlet()
font_list = figlet.getFonts()


if len(sys.argv) == 1:
    user_input = input("Input: ")
    font = random.choice(font_list)
    f = Figlet(font=font)
    print(f"Output: {f.renderText(user_input)}")
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in font_list:
    user_input = input("Input: ")
    font = random.choice(font_list)
    f = Figlet(font=sys.argv[2])
    print(f"Output: {f.renderText(user_input)}")
else:
    sys.exit("Invalid usage")
