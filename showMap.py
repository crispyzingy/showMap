# place the showmap.bat file in the python script path

import sys
import webbrowser

import pyperclip

sys.argv  # ['showMap.py, '870', 'Valencia', 'St.]

# Check if command line arguments were passed
if len(sys.argv) > 1:
    # ['showMap.py, '870', 'Valencia', 'St.] -> '850 Valencia St'
    address = " ".join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open("https://www.google.com/maps/place/" + address)
