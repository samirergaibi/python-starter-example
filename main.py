import pyperclip

print("""
*-----------------------------------------------------------------------------*
| Check the README.md for instructions on how to setup a virtual environment. |
*-----------------------------------------------------------------------------*
""")

clipboard = pyperclip.paste()
print("Your clipboard contains:")
print(clipboard)

# Importing from the local utils folder
from utils.math import add
print(add(1, 2))