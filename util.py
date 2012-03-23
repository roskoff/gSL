
def formatTree(text):
    formatted = ""
    indentation = 0
    i = 0
    while i < len(text):
        s = text[i]
        if s in "[(" and text[i + 1] not in ")]":
            indentation += 4
            formatted += "\n" + (indentation * " ")
        elif s in ")]" and text[i - 1] not in "([":
            indentation -= 4
            formatted += "\n" + (indentation * " ")
        elif s in ",":
            formatted += "\n" + (indentation * " ")

        formatted += s

        i += 1

    return formatted


if __name__ == "__main__":
    print formatTree("FunctionDef(name = 'imprimir', args = arguments(args   = [], vararg = 'args', kwarg  = None, defaults = []), body = [For(target = Name(id = 'arg', ctx=Store()), iter   = Name(id = 'args', ctx=Load()), body   = [Print(dest = None, values = [Name(id = 'arg', ctx=Load())], nl=False)], orelse=[]), Print(dest=None, values=[], nl=True)], decorator_list=[])")

