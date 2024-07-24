import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):    
    # def test_SC401(self):
    #     input = Program([
    #         VarDecl("x", AutoType()),
    #         FuncDecl("main", VoidType(), [], None, BlockStmt([]))
    #     ])
    #     expect = "Invalid Variable: x"
    #     self.assertTrue(TestChecker.test(input, expect, 400))
        
    def test2(self):
        input = """
        a: float;
        b: function string (a: integer, b: float, c: string) inherit c{
            super();
        }
        c: function void (a: string){}
        """
        self.assertTrue(TestChecker.test(input, "", 401))
    # def test_SC402(self):
    #     input = Program([
    #         VarDecl("x", BooleanType(), IntegerLit(1))
    #     ])
    #     expect = "Type mismatch in Variable Declaration: VarDecl(x, BooleanType, IntegerLit(1))"
    #     self.assertTrue(TestChecker.test(input, expect, 401))
    
    # def test_3(self):
    #     input = Program([
    #         VarDecl("x", IntegerType(), IntegerLit(1)),
    #         FuncDecl("main", VoidType(), [], None, BlockStmt([]))
    #     ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 402))