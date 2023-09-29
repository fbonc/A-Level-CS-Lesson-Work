import re
txt = "WU65 GJV"

def validate_reg(str: str):
    match = re.search('^[A-Z]{2}[0-9]{2} [A-Z]{3}$', txt)
    return match

print(validate_reg(txt))

