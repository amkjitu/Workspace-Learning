from input_handler import input_handler
from Parser import Parser

def main():
    CFG, input_string = input_handler()
    Parser(CFG, input_string)


main()