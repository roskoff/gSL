#from .gSLParser import gSLParser
from gSLParser import yacc

if __name__ == "__main__":
    import pprint
    import time, sys

    #t1 = time.time()
    #parser = gSLParser()
    #sys.write(time.time() - t1)
				    
    #buf = ''' 
        #int (*k)(int);
    #'''
    file = open('./tests/test.sl')
    contents = file.read()
						        
    t = yacc.parse(contents)
    #t.show(showcoord=True)
