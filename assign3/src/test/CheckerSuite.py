import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):    
    
    def test2(self):
        input = """
        x: boolean;
        bar: function auto(){
            if(x) return 1;
            return 1.0;
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 401))
        
    # def test_SC404(self):
    #     input = """
    #     foo: function void() inherit ain{
    #         super(14);        
    #     }
    #     ain:function void (inherit y: auto) {
    #         f: array[3] of float;
    #         f[4.3] = 1;
    #     }"""
    #     expect = "Type mismatch in expression: ArrayCell(f, [FloatLit(4.3)])"
    #     self.assertTrue(TestChecker.test(input, expect, 404))

    # def test_SC405(self):
    #     input = Program([VarDecl("a", IntegerType()),
    #                     VarDecl("c", FloatType())])
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_SC406(self):
    #     input = """
    #     foo: function void() inherit ain{
    #         super(14);        
    #     }
    #     ain:function void (inherit y: auto) {
    #         f: array[3] of float;
    #     }"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 406))

    # def test_SC407(self):
    #     input = """
    #     foo: function void() inherit ain{
    #         super(14);        
    #     }
    #     ain:function void (inherit y: auto) {
    #         f: array[3] of float;
    #     }
    #     main: function float(){        
    #     }"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 407))

    # def test_SC408(self):
    #     input = """
    #     foo: function void() inherit ain{
    #         super(14);        
    #     }
    #     ain:function void (inherit y: auto) {
    #         f: array[3] of float;
    #     }
    #     main: function void(x: auto){        
    #     }"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 408))

    # def test_SC409(self):
    #     input = """
    #     foo: function void() inherit ain{
    #         super(14);        
    #     }
    #     ain:function void (inherit y: auto) {
    #         f: array[3] of float;
    #     }
    #     main: function void(){        
    #     }"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 409))

    # def test_SC410(self):
    #     input = """
    #     foo: function void() inherit ain{
    #         super(14,1);        
    #     }
    #     ain:function void (inherit y: auto) {
    #         f: array[3] of float;
    #     }
    #     main: function auto(){        
    #     }"""
    #     expect = "Type mismatch in expression: IntegerLit(1)"
    #     self.assertTrue(TestChecker.test(input, expect, 410))

    # def test_SC429(self):
    #     input = """
    #     x: integer = 1;
    #     main: function void() inherit foo{
    #         super("!");
    #         f: array[5] of integer = {1,2,3,4,5};
    #         g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
    #     }
    #     foo: function float(inherit x: float){}"""
    #     expect = "Type mismatch in expression: StringLit(!)"
    #     self.assertTrue(TestChecker.test(input, expect, 429))