import config
from tkinter import *  # py3
#from Tkinter import *  # py2
import random
import time
from firebase import Firebase
print("past imports")
# must:
#  pip install:
#   firebase
#   python_jwt
#   gcloud
#   sseclient
#   pycryptodome
#   requests_toolbelt

DEFAULT_HR = 70


def close_window(root):
    root.destroy()


base_20yrold_athletic_rest_hr = 40
base_20_yrold_target_exer_hr = 100
max_20_yrold_target_exer_hr = 170

base_30_yrold_target_exer_hr = 95
max_30_yrold_target_exer_hr = 162


def change_color(root, database):
    hex_color = get_hr_value(database)

    root.configure(bg=hex_color)

    # call this function again in one second
    root.after(200, change_color, root, db)


def convert_val_to_color(hr):
    # ranges of rainbow, uses color_variant to lighten colors away from base color for that
    #  range -- P.S. however a better approach would be to average and lighten toward the gradient
    #  of tier above and tier below percentage...
    print(type(hr))
    if hr >= 160:
        rtn = color_variant("#FF0000", int(hr / 160))  # "red range"
    #elif hr >= 140:
    #    rtn = color_variant("#FF7F00", int(hr / 140))  # "orange range" # nope
    #elif hr >= 115:
    #    rtn = color_variant("#FFFF00", int(hr / 115))  # "yellow range" # nope
    #elif hr >= 85:
    #    rtn = color_variant("#00FF00", int(hr / 85))  # "green range" # nope
    elif hr >= 65:
        rtn = color_variant("#0000FF", int(hr / 65))  # "blue range"
    elif hr >= 55:
        rtn = color_variant("#4B0082", int(hr / 55))  # "indigo range"
    elif hr >= 40:
        rtn = color_variant("#9400D3", int(hr / 40)) # "violet range"
    else:
        rtn = "#9400D3"
    print(rtn)
    return rtn
    # these / divisions should maybe be 1.0 - (hr/top)...


def color_variant(hex_color, brightness_offset=1):
    """
    takes a color like #87c95f and produces a lighter or darker variant \
    https://chase-seibert.github.io/blog/2011/07/29/python-calculate-lighterdarker-rgb-colors.html
    """
    if len(hex_color) != 7:
        raise Exception("Passed %s into color_variant(), needs to be in #87c95f format." % hex_color)
    rgb_hex = [hex_color[x:x + 2] for x in [1, 3, 5]]
    new_rgb_int = [int(hex_value, 16) + brightness_offset for hex_value in rgb_hex]
    new_rgb_int = [min([255, max([0, i])]) for i in new_rgb_int]  # make sure new values are between 0 and 255
    # hex() produces "0x88", we want just "88"
    rtn = "#"
    for i in new_rgb_int:
        _byte = hex(i)[2:]
        if len(_byte) == 1:
            _byte = '0' + _byte  # need 01, not just 1 for #_______
        rtn += _byte
    print(rtn)
    return rtn


def get_hr_value(database):
    """
    pulls hr values from somewhere
    :return: hex color
    """
    hr_req_val = database.child("hr").get().val()
    if hr_req_val:
        return convert_val_to_color(hr_req_val)
    else:
        return convert_val_to_color(DEFAULT_HR)


# initialize random
random.seed(time.localtime())

config_f = {
  "apiKey": config.api_key,
  "authDomain": config.authDomain,
  "databaseURL": config.databaseURL,
  "storageBucket": config.storageBucket
}

# initialize firebase
firebase = Firebase(config_f)
db = firebase.database()

# tkinter UI setup and start
window = Tk()
window.title("")
window.configure(bg="blue")
window.overrideredirect(True)
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
change_color(window, db)
# press q to quit
window.bind("<q>", lambda event, root=window: close_window(root))
window.focus_set()

window.mainloop()
