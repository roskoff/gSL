# -*- coding: utf-8 -*-

# Esta función retorna las funciones necesarias para
# poder debugguear código python
def getDebugFunctions():
    from ast import Import, alias, Expr, Call, Attribute, Load, Name
    functions = []

    functions.append(Import(names=[alias(asname=None,
                                 name='pdb')]))
    functions.append(Expr(value=Call(args=[],
                             func=Attribute(attr='set_trace',
                                            ctx=Load(),
                                            value=Name(ctx=Load(),
                                                       id='pdb')),
                             keywords=[],
                             kwargs=None,
                             starargs=None)))

    return functions
