import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):    
    
    def test2(self):
        input = """
        x: float;
        
        b: function string (a: auto, b: float, c: string) inherit c{
            //super("a", 5);
            preventDefault();
            c();
        }
        c: function void (o: string, m: integer){}
        """
        expect = "Type mismatch in statement: CallStmt(c, )"
        self.assertTrue(TestChecker.test(input, expect, 401))
        
