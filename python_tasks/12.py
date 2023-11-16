import re
def check_string(string):
    pattern = re.compile(r"((\+(?=7))?[78]?[- ]?[\( ]?\d{3}[\) ]?[- ]?\d{3}-?\d{2}-?\d{2})|"
                        r"(\w+(\.\w{2,})*@\w+(\.\w{2,})+)")
    return bool(pattern.fullmatch(string))