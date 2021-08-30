COLOUR_TO_HEX = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "black": "#000000", "blueviotlet": "#8a2be2",
                 "brown": "#a52a2a", "burlywood": "#deb887", "cadetblue": "#5f9ea0"}
print(COLOUR_TO_HEX)

colour_name = input("Enter colour name: ")
while colour_name != "":
    if colour_name in COLOUR_TO_HEX:
        print(colour_name, "is", COLOUR_TO_HEX[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ")

for key, value in COLOUR_TO_HEX.items():
    print(key, "is", value)
