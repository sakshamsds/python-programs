# -*- coding: utf-8 -*-

import webbrowser as web
import sys, pyperclip

sys.argv    # ['mapit.py', '870', 'Valencia', 'St.']+

# Check if cmd line args were passed
if len(sys.argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])
else: 
    address = pyperclip.paste()
    print(address)

# https://www.google.com/maps/place/<ADDRESS>
web.open('https://www.google.com/maps/place/' + address)
