import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):    
    
    def test1(self):
        input = """x: integer;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 400))
        
    def test2(self):
        input = """x: float = 1.555;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 401))
        
    def test3(self):
        input = """x: auto;"""
        expect = "Invalid Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 402))
        
    def test4(self):
        input = """x: array[5] of integer = {1,2,3,4,5};"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 403))
    
    def test5(self):
        input = """x: auto = false;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 404))
    
    def test6(self):
        input = """
        x: array[5] of integer = {1,2,3,4,5};
        x: auto;
        """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 405))
        
    def test7(self):
        input = """
        foo: function void() inherit bar {
            super(10);
            x: integer = 1;
        }
        bar: function void(x: integer) {}
        main: function void() {
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test8(self):
        input = """
        foo: function void() inherit bar {
            super(10, 1);
        }
        bar: function void(inherit x: integer, y: integer) {}
        main: function void() {
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test9(self):
        input = """
        foo: function void() inherit bar {
            super(1.0);
        }
        bar: function void(inherit x: float) {}
        main: function void() {
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test10(self):
        input = """
        main: function void() {
            foo: array[5] of integer = {1, 2, 3, 4, 5};
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test11(self):
        input = """
        foo: function void(x: integer) {
            y: float = 1.0;
            x = y;
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(x), Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 410))
    
    def test12(self):
        input = """
        foo: function boolean() inherit goo{
            super(5);        
        }
        goo:function float ( a: integer) {
            b: array[5] of string;
        }
        main: function auto(){        
        }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test13(self):
        input = """
        foo: function auto(){
            super(3.14, 5);
        }
        bar:function void (inherit a: float, inherit b: integer) {
            c: array[5,5] of float;
        }
        main: function void(){        
        }"""
        expect = "Type mismatch in statement: CallStmt(super, FloatLit(3.14), IntegerLit(5))"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test14(self):
        input = """
        foo: function void(){
            bar();       
        }
        foo1:function auto (inherit x: float, inherit y: integer) {
            x: float = 1;
        }
        main: function void(){        
        }"""
        expect = "Undeclared Function: bar"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test15(self):
        input = """
        foo: function void(){
            foo1(3,4,5);       
        }
        foo1:function boolean (x: float, y: integer) {
            arr: array[5] of integer;
        }
        main: function void(){        
        }"""
        expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(3), IntegerLit(4), IntegerLit(5))"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test16(self):
        input = """
        main: function void(){
            arr: array[2,2] of integer = { {1,2}, {3,4} };      
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test17(self):
        input = """
        foo: function void() inherit bar{
            preventDefault();
        }
        bar:function void (inherit a: float, inherit a: integer) {
            arr: array[2,2] of integer = { {1,2}, {3,4} };      
        }
        main: function void(){
        }"""
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test18(self):
        input = """
        main: function void(){
            arr: array[2] of integer = {1,2,3,4,5};
            arr1: array[1,2,3] of float = {{{1,2,3},{4,5,6}}};
        }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(arr, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test19(self):
        input = """
        main: function void(){
            arr: array[1,2,3] of integer = {{{1,2,3,4},{4,5,6}}};
        }"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)])])])"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test20(self):
        input = """
        main: function void(){
            arr: array[5] of integer = {1,2,3,4,5};
            arr1: array[1,2,3] of float = {{{1,2,"34"},{4,5,6}}};
        }"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), StringLit(34)]), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)])])])"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test21(self):
        input = """
        main: function void(){
            arr: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test22(self):
        input = """
        a: integer = 1;
        main: function void(){
            arr: array[5] of integer = {1,2,3,4,5};
            brr: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            brr[1,2,1] = "1";
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test23(self):
        input = """
        a: integer = 1;
        main: function void(){
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of string = {{{"1","2","34"},{"4","5","6"}}};
            g[a, b, c] = "1";
        }"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test24(self):
        input = """
        a: integer = 1;
        main: function void(){
            f: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of boolean = {{{true, true, false},{false, false, false}}};
            g[x,f,r] = true;
        }"""
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test25(self):
        input = """
        x: float = 1;
        main: function void(){
            g: array[1,2,3] of boolean = {{{true, true, false},{false, false, false}}};
            g[x,1] = true;
        }"""
        expect = "Type mismatch in expression: ArrayCell(g, [Id(x), IntegerLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test26(self):
        input = """
        x: integer = 1;
        main: function void() inherit foo{
            super(12);
            arr: array[5] of integer = {1,2,3,4,5};
            g: array[1,2,3] of boolean = {{{true, true, false},{false, false, false}}};
            g[x,1,x] = false;            
        }
        foo: function float(inherit x: float){}"""
        expect = "Type mismatch in expression: ArrayCell(g, [Id(x), IntegerLit(1), Id(x)])"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test27(self):
        input = """
        x: integer = 1;
        main: function void() inherit foo{
            preventDefault();
            x: float = 2.222222;        
        }
        foo: function integer(inherit x: float){}"""
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test28(self):
        input = """
        x: integer = 1;
        main: function void() inherit foo{ 
        }
        foo: function float(inherit x: float){}"""
        expect = "Invalid statement in function: main"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test29(self):
        input = """
        x: integer = 1;
        main: function void() inherit foo{
            preventDefault();
            {
                abc: string = "abc";
            }         
        }
        foo: function float(){}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test30(self):
        input = """
        boo: function void() inherit foo{
            super("!");
        }
        foo: function auto(inherit x: float){}"""
        expect = "Type mismatch in expression: StringLit(!)"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test31(self):
        input = """
        x: string = "abc";
        main: function void(){
            if (x == "1") x = 1;            
        }
        """
        expect = "Type mismatch in expression: BinExpr(==, Id(x), StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 430))
    
    def test32(self):
        input = """
        foo: function void() inherit bar{
            
        }
        bar: float = 5/123;
        """
        expect = "Undeclared Function: bar"
        self.assertTrue(TestChecker.test(input, expect, 431))
        
    def test33(self):
        input = """
        foo: function void() inherit bar{
            
        }
        bar: function void(a: boolean){}
        """
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, expect, 432))
        
    def test34(self):
        input = """
        foo: function void() inherit bar{
            
        }
        bar: function void(){}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 433))
        
    def test35(self):
        input = """
        foo: function void(){
            bar(true);
        }
        bar: function void(a: boolean){}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 434))
        
    def test36(self):
        input = """
        foo: function void(){
            bar(true,4);
        }
        bar: function void(a: boolean){}
        """
        expect = "Type mismatch in statement: CallStmt(bar, BooleanLit(True), IntegerLit(4))"
        self.assertTrue(TestChecker.test(input, expect, 435))
        
    def test37(self):
        input = """
        foo: function void(){
            bar();
        }
        bar: function void(a: boolean){}
        """
        expect = "Type mismatch in statement: CallStmt(bar, )"
        self.assertTrue(TestChecker.test(input, expect, 436))
    
    def test38(self):
        input = """
        x: float = 3.14;
        foo : function integer (n : integer) {
            if (n < 10) {}
            else {}
        }
        main: function void(){}
    """

        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test39(self):
        input = """
        foo: function void (){
            x: integer;
            {
                x = 5;
            }
        }
        main: function void(){}
    """

        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test40(self):
        input = """
        x: float = 3.14;
        a : array [5] of integer;
        foo : function auto (n : integer) {
            n = n+x;
            a[1] = 3;    
        }
        main: function void(){}
    """

        expect = "Type mismatch in statement: AssignStmt(Id(n), BinExpr(+, Id(n), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test41(self):
        input = """
        foo: function auto(){}
        fact : function integer (n : integer) {
            n = readInteger();
        }
        main: function void(){}
    """

        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test42(self):
        input = """
        main: function void(){
            printInteger(234);
            x: auto = -readFloat();
            printString(x);
        }
    """

        expect = "Type mismatch in statement: CallStmt(printString, Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test43(self):
        input = """
        foo: function auto(x: integer){
            y: float = bar();
        }
        bar: function void (){
        }
        main: function void(){}
    """

        expect = "Type mismatch in expression: FuncCall(bar, [])"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test44(self):
        input = """
            foo: function void(){
                x: boolean;
                {
                    x: float;
                }
                x = 5.5;
            }
            main: function void(){}
        """
        expect = "Type mismatch in statement: AssignStmt(Id(x), FloatLit(5.5))"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test45(self):
        input = """
            foo: function void (){
                return 1;
            }
        """

        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test46(self):
        input = """
        foo: function integer(a: integer){
            x: string = "hello world!";
            return a;
            return x;
        }

        main: function void(){}
    """

        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test47(self):
        input = """
            foo: function integer(a: integer){
            x: string = "hello world!";
            return x;
            return a;
        }
        main: function void(){}
        """
        expect = "Type mismatch in statement: ReturnStmt(Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test48(self):
        input = """

        a: integer;
        foo1: function integer(inherit x: float){}

        foo2: function float(inherit y: float) inherit foo1{
            super(10);
            z: float = 10.1;
            return 1;
        }
        foo3: function float(out z: float) inherit foo2{
            preventDefault();
            y: integer = 10;
            printInteger(1);
            return 1.123;
        }

        main: function void(){
            x: integer = readInteger();
        }
    """
        expect = "Redeclared Variable: y"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test49(self):
        input = """
        main: function void(){
            x: integer = readInteger();
            if (x>5){
                return x;
            }
            return 5;
        }
    """

        expect = "Type mismatch in statement: ReturnStmt(Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test50(self):
        input = """
        foo: function auto(){
            x: integer = readInteger();
            y: float = 3.14;
            if (x>5){
                return x;
            }
            return y;
        }
    """

        expect = "Type mismatch in statement: ReturnStmt(Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test51(self):
        input = """
        foo: function void(){
            return;
        }
        main: function void(){
            foo();
        }
    """

        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 450))
        
    def test51(self):
        input = """
        main: function void(){
            arr: array[2,2] of integer;
            arr[0] = {1,2};
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 451))
        
    def test52(self):
        input = """
        foo: function array[5] of integer(n: integer){
            return {n, n+1, n+2, n+3, n+4};
            return None;
        }
        main: function void(){
            arr: array[5] of integer;
            arr = foo(5);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 452))
        