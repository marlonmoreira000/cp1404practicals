"""This program finds the hexadecimal number for a colour of the user's choosing"""

PAINT_COLOUR_TO_HEX_NUMBER = {"AliceBlue": "f0f8ff", "bisque1": "#ffe4c4", "beige": "#f5f5dc", "blue1": "#0000ff",
                              "CadetBlue1": "#98f5ff", "chocolate": "#d2691e", "cyan1": "#00ffff", "gray20": "#333333"}

colour_name = str(input("Colour name: "))
while colour_name != "":
    if colour_name in PAINT_COLOUR_TO_HEX_NUMBER:
        print(PAINT_COLOUR_TO_HEX_NUMBER[colour_name])
    else:
        print("Enter a valid colour name.")
    colour_name = str(input("Colour name: "))
