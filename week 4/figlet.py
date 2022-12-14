import sys
import pyfiglet


if sys.argv[1] != '-f' or len(sys.argv)<2:
    sys.exit("Invalid usage")
else:
    user_input = input()
    result = pyfiglet.figlet_format(user_input, font = sys.argv[2])
    print(result)
