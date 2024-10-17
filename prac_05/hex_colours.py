COLOUR_TO_HEX = {
    "aliceblue": "#f0f8ff",
    "amber": "#ffbf00",
    "aqua": "#00ffff",
    "beaver": "#9f8170",
    "beige": "#f5f5dc",
    "brass": "#b5a642",
    "camel": "#c19a6b",
    "carmine": "#960018",
    "corn": "#fbec5d",
    "denim": "#1560bd",
}
colour_name = input("Colour name: ").lower()
while colour_name != "":
    try:
        print(COLOUR_TO_HEX[colour_name])
    except KeyError:
        print("Colour not found :(")
    colour_name = input("Colour name: ").lower()