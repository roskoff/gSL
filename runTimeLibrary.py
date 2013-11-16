# -*- coding: utf-8 -*-

# Esta función retorna todas las funciones predeterminadas en SL, el
# conjunto de todas ellas sería nuestro RunTime Library (RTL)
def getFunctions():
    from ast import FunctionDef, For, Print, Name, Load, Store, Assign, Call, Attribute, arguments
    from ast import Str, If, Compare, NotEq, Raise, Num, While, Param, Gt, Tuple
    from ast import Lt, Subscript, Add, Index, AugAssign, ListComp, comprehension
    from ast import Import, alias, Eq, Or, BoolOp
    functions = []

    # imprimir(...)
    # Recibe cero o mas expresiones separadas por coma y las
    # imprime en pantalla separadas por un espacio
    #
    # Código Python
    # def imprimir(*args):
    #     for arg in args:
    #         print arg,
    #     print
    #
    functions.append(FunctionDef(name = 'imprimir',
                                args = arguments(args   = [],
                                                 vararg = 'args',
                                                 kwarg  = None,
                                                 defaults = []),
                                body = [For(target = Name(id = 'arg', ctx=Store()),
                                            iter   = Name(id = 'args', ctx=Load()),
                                            body   = [Print(dest = None, values = [Name(id = 'arg', ctx=Load())], nl=False)],
                                            orelse=[]),
                                        Print(dest=None, values=[], nl=True)],
                                decorator_list=[]))
    # leer(...)
    # Lee uno o mas valores y los asigna a las variables que
    # se pasan como parámetros
    #
    # Código Python
    #def leer(l):
    #    import inspect
    #    input_values = raw_input()
    #    list_values = input_values.split(',')
    #    count_values = len(list_values)
    #    #if len(list(l.iteritems())) > count_values:
    #    if len(l) > count_values:
    #        raise Exception("Error de ejecución, ya no hay datos de entrada para la función leer()")
    #    caller_locals = inspect.currentframe().f_back.f_locals
    #    for i, v in enumerate(l):
    #        #TO-DO: Corregir para otros tipos de datos
    #        if v['tipo'] == type(1.0) or v['tipo'] == type(1):
    #            caller_locals[v['nombre']] = float(list_values[i])
    #        elif v['tipo'] == type('a'):
    #            caller_locals[v['nombre']] = list_values[i]
    functions.append(
FunctionDef(name='leer', args=arguments(args=[Name(id='l', ctx=Param())], vararg=None, kwarg=None, defaults=[]), body=[Import(names=[alias(name='inspect', asname=None)]), Assign(targets=[Name(id='input_values', ctx=Store())], value=Call(func=Name(id='raw_input', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Name(id='list_values', ctx=Store())], value=Call(func=Attribute(value=Name(id='input_values', ctx=Load()), attr='split', ctx=Load()), args=[Str(s=',')], keywords=[], starargs=None, kwargs=None)), Assign(targets=[Name(id='count_values', ctx=Store())], value=Call(func=Name(id='len', ctx=Load()), args=[Name(id='list_values', ctx=Load())], keywords=[], starargs=None, kwargs=None)), If(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='l', ctx=Load())], keywords=[], starargs=None, kwargs=None), ops=[Gt()], comparators=[Name(id='count_values', ctx=Load())]), body=[Raise(type=Call(func=Name(id='Exception', ctx=Load()), args=[Str(s='Error de ejecuci\\xc3\\xb3n, ya no hay datos de entrada para la funci\\xc3\\xb3n leer()')], keywords=[], starargs=None, kwargs=None), inst=None, tback=None)], orelse=[]), Assign(targets=[Name(id='caller_locals', ctx=Store())], value=Attribute(value=Attribute(value=Call(func=Attribute(value=Name(id='inspect', ctx=Load()), attr='currentframe', ctx=Load()), args=[], keywords=[], starargs=None, kwargs=None), attr='f_back', ctx=Load()), attr='f_locals', ctx=Load())), For(target=Tuple(elts=[Name(id='i', ctx=Store()), Name(id='v', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='enumerate', ctx=Load()), args=[Name(id='l', ctx=Load())], keywords=[], starargs=None, kwargs=None), body=[If(test=BoolOp(op=Or(), values=[Compare(left=Subscript(value=Name(id='v', ctx=Load()), slice=Index(value=Str(s='tipo')), ctx=Load()), ops=[Eq()], comparators=[Call(func=Name(id='type', ctx=Load()), args=[Num(n=1.0)], keywords=[], starargs=None, kwargs=None)]), Compare(left=Subscript(value=Name(id='v', ctx=Load()), slice=Index(value=Str(s='tipo')), ctx=Load()), ops=[Eq()], comparators=[Call(func=Name(id='type', ctx=Load()), args=[Num(n=1)], keywords=[], starargs=None, kwargs=None)])]), body=[Assign(targets=[Subscript(value=Name(id='caller_locals', ctx=Load()), slice=Index(value=Subscript(value=Name(id='v', ctx=Load()), slice=Index(value=Str(s='nombre')), ctx=Load())), ctx=Store())], value=Call(func=Name(id='float', ctx=Load()), args=[Subscript(value=Name(id='list_values', ctx=Load()), slice=Index(value=Name(id='i', ctx=Load())), ctx=Load())], keywords=[], starargs=None, kwargs=None))], orelse=[If(test=Compare(left=Subscript(value=Name(id='v', ctx=Load()), slice=Index(value=Str(s='tipo')), ctx=Load()), ops=[Eq()], comparators=[Call(func=Name(id='type', ctx=Load()), args=[Str(s='a')], keywords=[], starargs=None, kwargs=None)]), body=[Assign(targets=[Subscript(value=Name(id='caller_locals', ctx=Load()), slice=Index(value=Subscript(value=Name(id='v', ctx=Load()), slice=Index(value=Str(s='nombre')), ctx=Load())), ctx=Store())], value=Subscript(value=Name(id='list_values', ctx=Load()), slice=Index(value=Name(id='i', ctx=Load())), ctx=Load()))], orelse=[])])], orelse=[])], decorator_list=[])
            )

    return functions
