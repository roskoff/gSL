import unittest
try:
    import StringIO
except ImportError:
    import io as StringIO

import sys
if "../.." not in sys.path: sys.path.insert(0,"../..")

def check_expected(result,expected):
    if sys.version_info[0] >= 3:
        if isinstance(result,str):
            result = result.encode('ascii')
        if isinstance(expected,str):
            expected = expected.encode('ascii')
    resultlines = result.splitlines()
    expectedlines = expected.splitlines()

    if len(resultlines) != len(expectedlines):
        return False

    for rline,eline in zip(resultlines,expectedlines):
        if not rline.endswith(eline):
            return False
    return True

def run_import(module):
    code = "import "+module
    exec(code)
    del sys.modules[module]

class TestAST(unittest.TestCase):
    def setUp(self):
        sys.stderr = StringIO.StringIO()
        sys.stdout = StringIO.StringIO()
    def tearDown(self):
        sys.stderr = sys.__stderr__
        sys.stdout = sys.__stdout__

    def test_syn_01_empty_program(self):
        run_import("syn_01_empty_program")
        result = sys.stdout.getvalue()
        self.assert_(check_expected(result,
#        self.assertEquals(result,
                                    "Module(body=[])\n")
                     )

    def test_syn_02_empty_named_program(self):
        run_import("syn_02_empty_named_program")
        result = sys.stdout.getvalue()
        self.assert_(check_expected(result,
#        self.assertEquals(result,
                                    "Module(body=[Expr(value=Str(s='nombre_programa'))])\n")
                     )

    def test_syn_03_empty_program_comments(self):
        run_import("syn_03_empty_program_comments")
        result = sys.stdout.getvalue()
        self.assert_(check_expected(result,
#        self.assertEquals(result,
                                    "Module(body=[Expr(value=Str(s='nombre_programa'))])\n")
                     )

if __name__ == '__main__':
    unittest.main()
