#!../../bin/python3
# bullet_point_adder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()

# Seperate lines and add stars.
lines = text.split('\n')
for i, line in enumerate(lines):     # loop through all indexes in the 'lines' list
    lines[i] = f'* {lines[i]}'  # add star to each string in 'lines' list
text = '\n'.join(lines)
pyperclip.copy(text)

print(pyperclip.paste())