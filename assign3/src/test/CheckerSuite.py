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
        
    def test52(self):
        input = """
        main: function void(){
            arr: array[2,2] of integer;
            arr[0] = {1,2};
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 451))
        
    def test53(self):
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
        
    def test54(self):
        input = """
        main: function void(){
            arr: array[5] of integer = {1,2,3};
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(arr, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"
        self.assertTrue(TestChecker.test(input, expect, 453))
        
    def test55(self):
        input = """
        main: function void(a: auto){
            x: integer = a + bar();
        }
        foo: function auto(){
            return 5;
        }
        bar: function auto(){
            return true;
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 454))
        
    def test56(self):
        input = """
        main: function void(a: auto){
            x: string;
            x = foo() + bar();
        }
        foo: function auto(){
            return 5;
        }
        bar: function auto(){
            return true;
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(x), BinExpr(+, FuncCall(foo, []), FuncCall(bar, [])))"
        self.assertTrue(TestChecker.test(input, expect, 455))
        
    def test57(self):
        input = """
        main: function void(a: auto){
            x: float = -foo();
        }
        foo: function auto(){
            return true;
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 456))
        
    def test58(self):
        input = """
        main: function void(a: auto){
            x: float;
            x = !foo();
        }
        foo: function auto(){
            return true;
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(x), UnExpr(!, FuncCall(foo, [])))"
        self.assertTrue(TestChecker.test(input, expect, 457))
        
    def test59(self):
        input = """
        main: function void(a: auto){
            x: string;
            x = -foo();
        }
        foo: function auto(){
            return true;
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(x), UnExpr(-, FuncCall(foo, [])))"
        self.assertTrue(TestChecker.test(input, expect, 458))
        
    def test60(self):
        input = """
        main: function void(){
            for(i = 0, i<10, i+1){
                break;
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 459))
        
    def test61(self):
        input = """
        main: function void(){
            x: integer = 5;
            do{
                x = x-1;
            }while(x>5);
            continue;
        }
        """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 460))
        
    def test62(self):
        input = """
        main: function void(){
            for(i = 0, i<10, i+1){
                for(j=i,j<i,j+1){
                    if(i==j) continue;
                }
                if (i==5) {
                    continue;
                }else{
                    break;
                }
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 461))
        
    def test63(self):
        input = """
        main: function void(){
            x: integer = 5;
            while(true){
                if (x>5) continue;
                x = x+1;
            }
            break;
        }
        """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 462))
    
    def test64(self):
        input = """
        foo: function void(){
            return 5;
        }
        main: function void(){
            foo();
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(5))"
        self.assertTrue(TestChecker.test(input, expect, 463))
      
    def test65(self):
        input = """
        foo: function string(){
            return "i love ppl!";
        }
        main: function void(){
            a: string = foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 464))
      
    def test66(self):
        input = """
        x: integer = 5;
        foo: function string(a: integer, b: float){
            return "i love ppl!";
        }
        main: function void(){
            {
                x: string = "abc";
            }
            a: string = foo(x+4, 3.14);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 465))
      
    def test67(self):
        input = """
        foo: function string (a: string, b: float) {
            c : integer = 2;
            d: float = c + 1;
            f : array [5] of string;
            f[1] = d + 2.5;
            return f[1];
        }
        main: function void() {}
        """
        expect = "Type mismatch in statement: AssignStmt(ArrayCell(f, [IntegerLit(1)]), BinExpr(+, Id(d), FloatLit(2.5)))"
        self.assertTrue(TestChecker.test(input, expect, 466))
      
    def test68(self):
        input = """
        foo: function void() {
            x: integer = 1;
            for (i = 0, i < 10, i + 1) {
                y: integer = i;
            }
            y = y + 1;
        }
        """
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input, expect, 467))
    
    def test69(self):
        input = """
        foo: function void() {
            x: float = 1.0;
            y: integer = x + 1;
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(y, IntegerType, BinExpr(+, Id(x), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test70(self):
        input = """
        foo: function void() {
            x: float = 1.0;
            y: integer = x - 1;
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(y, IntegerType, BinExpr(-, Id(x), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test71(self):
        input = """
        foo: function void() {
            x: float = 1.0;
            y: integer = x * 1;
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(y, IntegerType, BinExpr(*, Id(x), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test72(self):
        input = """
        foo: function void() {
            x: float = 1.0;
            y: integer = x / 1;
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(y, IntegerType, BinExpr(/, Id(x), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test73(self):
        input = """
        foo: function void() {
            x: float = 1.0;
            y: integer = x % 1;
        }
        """
        expect = "Type mismatch in expression: BinExpr(%, Id(x), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test74(self):
        input = """
        foo: function void() {
            x: float = 1.0;
            y: boolean = x == 1;
        }
        """
        expect = "Type mismatch in expression: BinExpr(==, Id(x), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test75(self):
        input = """
        foo: function void() {
            x: float = 1.0;
            y: boolean = x != 1;
        }
        """
        expect = "Type mismatch in expression: BinExpr(!=, Id(x), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 474))
    
    def test76(self):
        input = """
        foo: function integer(a: integer) {
            x: float = "string";
            return 1;
        }
        main: function void() {}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(x, FloatType, StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test77(self):
        input = """
        foo: function void() {
            return 1;
        }
        main: function void() {}
        """
        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test78(self):
        input = """
        foo: function integer(a: integer) {
            a: float = 1.5;
            return 1;
        }
        main: function void() {}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test79(self):
        input = """
        foo: function integer() {
            a: integer = 10;
            if (a == 10) {
                b: integer = 20;
            }
            return b;
        }
        main: function void() {}
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test80(self):
        input = """
        foo: function integer() {
            return foo(1, 2);
        }
        main: function void() {}
        """
        expect = "Type mismatch in expression: FuncCall(foo, [IntegerLit(1), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test81(self):
        input = """
        foo: function integer() {
            x: integer = "hello";
            return 1;
        }
        main: function void() {}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(x, IntegerType, StringLit(hello))"
        self.assertTrue(TestChecker.test(input, expect, 480))
    
    def test82(self):
        input = """
        foo: function integer(a: integer) {
            x: string = "hello world!";
            return x;
        }
        main: function void() {}
        """
        expect = "Type mismatch in statement: ReturnStmt(Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test83(self):
        input = """
        a: integer;
        foo1: function integer(inherit x: float) {}

        foo2: function float(inherit y: float) inherit foo1 {
            super(10);
            z: float = 10.1;
            return z + 1;
        }
        
        foo3: function float(out z: float) inherit foo2 {
            preventDefault();
            y: integer = 10;
            return y;
        }
        
        main: function void() {
            x: integer = readInteger();
        }
        """
        expect = "Redeclared Variable: y"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test84(self):
        input = """
        main: function void() {
            x: integer = 5;
            if (x > 5) {
                y: float = 10.0;
            }
            return y;
        }
        """
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test85(self):
        input = """
        a: integer;
        foo1: function void(inherit x: float) {}
        
        foo2: function void(inherit x: float) inherit foo1 {
            super(10);
            x: integer = 20;
        }
        
        main: function void() {}
        """
        expect = "Invalid Parameter: x"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test86(self):
        input = """
        foo: function void() {
            x: integer = 10;
            {
                x: float = 20.5; // redeclared variable in block scope
            }
            return x;
        }
        main: function void() {}
        """
        expect = "Type mismatch in statement: ReturnStmt(Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test87(self):
        input = """
        foo: function void() {
            for (i = 0, i < 10, i + 1) {
                i: float = 1.0; 
            }
        }
        main: function void() {}
        """
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test88(self):
        input = """
        foo: function integer(a: integer) {
            b: float = a; // type mismatch
            return b;
        }
        main: function void() {}
        """
        expect = "Type mismatch in statement: ReturnStmt(Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test89(self):
        input = """
        foo: function void() {
            arr: array [5] of integer;
            arr[6] = 10; 
        }
        main: function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test90(self):
        input = """
        foo: function void() {
            x: integer = 10;
            y: float = 20.0;
            z: integer = x + y; 
        }
        main: function void() {}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(z, IntegerType, BinExpr(+, Id(x), Id(y)))"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test91(self):
        input = """
        foo: function void() {
            a: integer = 10;
            b: integer = 20;
            if (a > b) {
                return a; // invalid return type
            }
            return "hello"; // invalid return type
        }
        main: function void() {}
        """
        expect = "Type mismatch in statement: ReturnStmt(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 490))
    
    def test92(self):
        input = """
        foo: function integer(a: integer) {
            if (a > 0) {
                return a;
            } else {
                return "negative"; // type mismatch
            }
        }
        main: function void() {}
        """
        expect = "Type mismatch in statement: ReturnStmt(StringLit(negative))"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test93(self):
        input = """
        foo: function void() {
            for (i = 0, i < 10, i + 1) {
                if (i == 5) {
                    break;
                }
            }
            return i; 
        }
        main: function void() {}
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test94(self):
        input = """
        foo: function void(a: integer, b: integer) {
            for (i = 0, i < a + b, i + 1) {
                a = i + 1;
            }
            return b;
        }
        main: function void() {
            foo(1, "string"); 
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test95(self):
        input = """
        foo: function void() {
            while (true) {
                break;
            }
            return "done"; 
        }
        main: function void() {}
        """
        expect = "Type mismatch in statement: ReturnStmt(StringLit(done))"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test96(self):
        input = """
        foo: function void() {
            do {
                a: integer = 5;
                if (a > 3) continue;
            } while (a < 10); 
        }
        main: function void() {}
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test97(self):
        input = """
        foo: function integer(a: integer, b: float) {
            return a + b;
        }
        main: function void() {
            x: integer = foo(5, 3.0); 
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(BinExpr(+, Id(a), Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test98(self):
        input = """
        foo: function void(a: integer) {
            while (a > 0) {
                a = a - 1;
                if (a == 2) break;
                if (a == 1) continue;
            }
            return a; 
        }
        main: function void() {}
        """
        expect = "Type mismatch in statement: ReturnStmt(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test99(self):
        input = """
        foo: function void() {
            for (i = 0, i < 10, i + 1) {
                for (j = 0, j < 5, j + 1) {
                    if (i + j == 10) return "done"; // type mismatch
                }
            }
        }
        main: function void() {}
        """
        expect = "Type mismatch in statement: ReturnStmt(StringLit(done))"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test100(self):
        input = """
        foo: function void() {
            for (i = 0, i < 10, i + 1) {
                printInteger(i);
                if (i == 5) {
                    return "midway"; // type mismatch
                }
            }
        }
        main: function void() {}
        """
        expect = "Type mismatch in statement: ReturnStmt(StringLit(midway))"
        self.assertTrue(TestChecker.test(input, expect, 499))