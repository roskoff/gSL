import sys
from gSLParser import yacc

if __name__ == "__main__":
    file = open('./input.txt')
    contents = file.read()

    t = yacc.parse(contents)

