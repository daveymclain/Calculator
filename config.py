button_width = 5
button_height = int(button_width / 2)
app_font = "Calibri {size}".format(size=str(int(button_width * 3)))
buttons_test_list = {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "0": "0",
        "*": "X",
        "x": "X",
        "X": "X",
        "\x08": "del",
        "/": "/",
        "-": "-",
        "+": "+",
        ".": ".",
        "\r": "=",
        # the last two entries are for the event.keysym check
        "Return": "=",
        "BackSpace": "del"

    }