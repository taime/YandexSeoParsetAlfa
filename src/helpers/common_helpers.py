
from printy import printy, raw_format


def strP(pos):
    if pos < 10:
        return "  " + str(pos)
    elif pos < 100:
        return " " + str(pos)
    else:
        return str(pos)


def printPosWithColor(pos, text):
    if pos < 11:
        raw_text = raw_format(strP(pos), "y>B") + raw_format(" [g]| ") + raw_format(text, "y>")
    elif pos < 30:
        raw_text = raw_format(strP(pos), "oB") + raw_format(" [g]| ") + raw_format(text, "o")
    else:
        raw_text = raw_format(strP(pos), "mB") + raw_format(" [g]| ") + raw_format(text, "m")
    print(raw_text)
