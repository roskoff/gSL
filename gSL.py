import sys
from gSLParser import yacc

if __name__ == "__main__":
    file = open(sys.argv[1])
    source_code = file.read()
    tree = yacc.parse(source_code, debug=0)

    exec compile(tree, "<gsl_source_code>", "exec")


