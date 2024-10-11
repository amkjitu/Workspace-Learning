import tkinter as tk
from tkinter import filedialog
from pathlib import Path


CFG_NON_TERMINAL_SEPARATOR = "::="
CFG_PRODUCTION_RULES_SEPARATOR = "|"
INPUT_STRING_END_SYMBOL = "$"


def input_handler():
    file_name = get_cfg_file()
    CFG = parse_file_to_cfg(file_name)
    input_string = get_input_string()

    return CFG, input_string


# -------------------------------------------------------------------------------------
#
#   Method asks user for file containing CFG.
#   Is uses tkinter library to provide file dialog.
#   It raises error if:
#       * provided file is not in .txt extension.
#
# -------------------------------------------------------------------------------------
def get_cfg_file():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    is_txt = Path(file_path).suffix == '.txt'

    print("Provided CFG file: {}".format(file_path))
    # File must be in .txt extension.
    if not is_txt:
        raise NameError("CFG file must be in .txt format.")

    return file_path


def parse_file_to_cfg(file_path):
    with open(file_path) as f:
        lines = f.readlines()

    CFG = {}
    for line in lines:
        line = line.strip()
        line = line.split(CFG_NON_TERMINAL_SEPARATOR)

        non_terminal = line[0].strip()
        validate_non_terminal(non_terminal, CFG)
        line.pop(0)

        production_rules = []
        for el in line:
            if non_terminal in el:
                raise SyntaxError(
                    "Error in non-terminal symbol {}. Left recursion is not supported!".format(non_terminal))

            if '|' in el:
                el = el.split(CFG_PRODUCTION_RULES_SEPARATOR)
                el = (x.strip() for x in el)
                validate_production_rule(el, non_terminal)
                production_rules += el
            else:
                el = el.strip()
                validate_production_rule(el, non_terminal)
                production_rules.append(el)

        CFG[non_terminal] = production_rules

    validate_CFG(CFG)
    return CFG


def validate_production_rule(rule, non_terminal):
    if rule == "":
        raise SyntaxError(
            "Error in non-terminal symbol {}. Production rule can not be empty!".format(non_terminal))

# -------------------------------------------------------------------------------------
#
#   Method responsible for validating non-terminal symbol.
#   It raises error if:
#       * non-terminal is not upper case letter.
#       * such non-terminal already exists in the CFG.
#
# -------------------------------------------------------------------------------------


def validate_non_terminal(non_terminal, CFG):
    if not non_terminal.isupper():
        raise SyntaxError(
            "Error in non-terminal symbol {}. Production rules must start with non-terminal symbols.".format(non_terminal))

    if non_terminal in CFG:
        raise SyntaxError(
            "Non-terminal symbol {} already exists in CFG!".format(non_terminal))


# -------------------------------------------------------------------------------------
#
#   Method responsible for validating CFG.
#   It raises error if:
#       * any production rule uses non-terminal symbol which is not declared.
#
# -------------------------------------------------------------------------------------
def validate_CFG(CFG):
    for key in CFG:
        production_rules = CFG[key]
        for production in production_rules:
            for el in production:
                if el.isupper() and not (el in CFG):
                    raise SyntaxError("Error in {}. Invalid CFG".format(el))


# -------------------------------------------------------------------------------------
#
#   Method asks user for input string.
#
# -------------------------------------------------------------------------------------
def get_input_string():
    input_string = input("Enter input string: ")
    validate_input_string(input_string)
    return input_string


# -------------------------------------------------------------------------------------
#
#   Method responsible for validating input string.
#   It raises error if:
#       * input is an empty string.
#       * last element of input string is not equal to INPUT_STRING_END_SYMBOL
#
# -------------------------------------------------------------------------------------
def validate_input_string(input_string):
    if input_string == "" or input_string[-1] != INPUT_STRING_END_SYMBOL:
        raise SyntaxError("Invalid input string")
