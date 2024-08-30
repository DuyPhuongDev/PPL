import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test1(self):
        input="""
        main: function void(){
            x: array[3] of integer = {1,2,3};
            i: integer;
            i = x[1];
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 501))
        
    def test2(self):
        input = """
        main: function void() {
            a: integer = 5;
            b: integer;
            b = a + 10;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 502))
    
    def test3(self):
        input = """
        main: function void() {
            arr: array[4] of integer = {1, 2, 3, 4};
            sum: integer = 0;
            i: integer;
            for (i = 0, i < 4, i + 1) {
                sum = sum + arr[i];
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 503))
    
    def test4(self):
        input = """
        fact: function integer(n: integer) {
            if (n == 0) return 1;
            return n*fact(n-1);
        }
        
        main: function void() {
            res: integer;
            res = fact(5);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test5(self):
        input = """
        main: function void() {
            x: integer = 10;
            y: integer;
            if (x > 5) {
                y = x * 2;
            } else {
                y = x + 2;
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test6(self):
        input = """
        main: function void() {
            x: float = 3.14;
            y: float;
            y = x * 2.0;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test7(self):
        input = """
        main: function void() {
            a: integer = 7;
            b: integer;
            b = a - 3;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test8(self):
        input = """
        main: function void() {
            x: boolean = true;
            y: boolean = false;
            z: boolean;
            z = x || y;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test9(self):
        input = """
        main: function void() {
            s: string = "Hello";
            t: string = "World";
            u: string;
            u = (s :: " ") :: t;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test10(self):
        input = """
        main: function void() {
            a: integer = 10;
            b: float = 5.5;
            c: float;
            c = a + b;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test11(self):
        input = """
        main: function void() {
            arr: array[3] of integer = {1, 2, 3};
            x: integer;
            x = arr[0] + arr[2];
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 511))

    def test12(self):
        input = """
        main: function void() {
            arr: array[2, 2] of integer = {{1, 2}, {3, 4}};
            y: integer;
            y = arr[1, 1];
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test13(self):
        input = """
        main: function void() {
            a: array[5] of float = {1.1, 2.2, 3.3, 4.4, 5.5};
            i: integer;
            s: float = 0.0;
            for (i = 0, i < 5, i + 1) {
                s = s + a[i];
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test14(self):
        input = """
        main: function void() {
            arr: array[2] of boolean = {true, false};
            x: boolean;
            x = arr[0] && arr[1];
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test15(self):
        input = """
        main: function void() {
            arr: array[4] of string = {"a", "b", "c", "d"};
            s: string;
            s = arr[1] :: arr[3];
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test16(self):
        input = """
        main: function void() {
            x: integer = 5;
            if (x > 3) {
                x = x + 1;
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 516))

    def test17(self):
        input = """
        main: function void() {
            y: float = 10.5;
            if (10<5) {
                y = y - 2.5;
            } else {
                y = y + 2.5;
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test18(self):
        input = """
        main: function void() {
            z: boolean = false;
            if (z == true) {
                z = false;
            } else {
                z = true;
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test19(self):
        input = """
        main: function void() {
            s: string = "Hello";
            if (true) {
                s = s :: " World";
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test20(self):
        input = """
        main: function void() {
            a: integer = 5;
            if ((a % 2) == 0) {
                a = a + 2;
            } else {
                a = a + 1;
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test21(self):
        input = """
        main: function void() {
            i: integer;
            for (i = 0, i < 5, i + 1) {
                x: integer = i * 2;
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test22(self):
        input = """
        main: function void() {
            sum: integer = 0;
            i: integer;
            for (i = 1, i <= 10, i + 1) {
                sum = sum + i;
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test23(self):
        input = """
        main: function void() {
            i: integer;
            for (i = 10, i > 0, i - 1) {
                y: integer = i - 1;
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 523))

    def test24(self):
        input = """
        main: function void() {
            x: integer = 1;
            i: integer;
            for (i = 2, i < 10, i + 2) {
                x = x * i;
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test25(self):
        input = """
        main: function void() {
            a: array[5] of integer = {1, 2, 3, 4, 5};
            i: integer;
            for (i = 0, i < 5, i + 1) {
                a[i] = a[i] * 2;
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test26(self):
        input = """
        main: function void() {
            i: integer = 0;
            while (i < 5) {
                i = i + 1;
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 526))

    def test27(self):
        input = """
        main: function void() {
            x: integer = 10;
            while (x > 0) {
                x = x - 2;
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 527))

    def test28(self):
        input = """
        main: function void() {
            y: float = 1.0;
            i: integer = 1;
            while (i<10) {
                y = y + 1.5;
                i=i+1;
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test29(self):
        input = """
        main: function void() {
            z: integer = 0;
            do {
                z = z + 1;
            } while (z < 3);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test30(self):
        input = """
        main: function void() {
            count: integer = 0;
            do {
                count = count + 2;
            } while (count <= 10);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test31(self):
        input = """
        sum: function integer(a: integer, b: integer) {
            return a + b;
        }
        
        main: function void() {
            x: integer;
            x = sum(5, 10);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test32(self):
        input = """
        max: function integer(a: integer, b: integer) {
            if (a > b) return a;
            return b;
        }
        
        main: function void() {
            y: integer;
            y = max(2, 5);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test33(self):
        input = """
        isEven: function boolean(n: integer) {
            return n % 2 == 0;
        }
        
        main: function void() {
            res: boolean;
            res = isEven(4);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test34(self):
        input = """
        concat: function string(s1: string, s2: string) {
            return s1 :: s2;
        }
        
        main: function void() {
            result: string;
            result = concat("Hello", "World");
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test35(self):
        input = """
        factorial: function integer(n: integer) {
            if (n == 0) return 1;
            else return n * factorial(n - 1);
        }
        
        main: function void() {
            fact: integer;
            fact = factorial(6);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 535))

    def test36(self):
        input = """
        main: function void() {
            i: integer;
            for (i = 0, i < 10, i + 1) {
                if (i == 5) break;
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test37(self):
        input = """
        main: function void() {
            j: integer = 0;
            while (j < 10) {
                if (j == 3) break;
                j = j + 1;
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test38(self):
        input = """
        main: function void() {
            k: integer;
            for (k = 0, k < 10, k + 1) {
                if ((k % 2) == 0) continue;
                k = k * 2;
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test39(self):
        input = """
        main: function void() {
            count: integer = 0;
            while (count < 10) {
                count = count + 1;
                if (count == 5) continue;
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 539))

    def test40(self):
        input = """
        main: function void() {
            n: integer = 0;
            do {
                if (n == 3) break;
                n = n + 1;
            } while (n < 5);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test41(self):
        input = """
        parentFunc: function void() {
            printString("Parent Function");
        }
        
        childFunc: function void() inherit parentFunc {
            super();
        }
        
        main: function void() {
            childFunc();
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test42(self):
        input = """
        parentFunc: function void() {
            printString("Parent Function");
        }
        
        childFunc: function void() inherit parentFunc {
            preventDefault();
            printString("Child Function");
        }
        
        main: function void() {
            childFunc();
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test43(self):
        input = """
        baseFunc: function void() {
            printString("Base Function");
        }
        
        derivedFunc: function void() inherit baseFunc {
            super();
            printString("Derived Function");
        }
        
        main: function void() {
            derivedFunc();
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test44(self):
        input = """
        baseFunc: function void() {
            printString("Base Function");
        }
        
        derivedFunc: function void() inherit baseFunc {
            preventDefault();
        }
        
        main: function void() {
            derivedFunc();
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test45(self):
        input = """
        ancestorFunc: function void() {
            printString("Ancestor Function");
        }
        
        parentFunc: function void() inherit ancestorFunc {
            super();
            printString("Parent Function");
        }
        
        childFunc: function void() inherit parentFunc {
            super();
            printString("Child Function");
        }
        
        main: function void() {
            childFunc();
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test46(self):
        input = """
        main: function void() {
            x: integer = 10;
            y: integer = 20;
            z: integer;
            z = x + y;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test47(self):
        input = """
        main: function void() {
            a: float = 5.5;
            b: float = 2.0;
            c: float;
            c = a * b;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test48(self):
        input = """
        main: function void() {
            p: boolean = true;
            q: boolean = false;
            r: boolean;
            r = p && q;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test49(self):
        input = """
        main: function void() {
            s1: string = "abc";
            s2: string = "def";
            s3: string;
            s3 = s1 :: s2;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test50(self):
        input = """
        main: function void() {
            arr: array[3] of integer = {1, 2, 3};
            i: integer = 1;
            result: integer;
            result = arr[i] + arr[i + 1];
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test51(self):
        input = """
        fibonacci: function integer(n: integer) {
            if (n == 0) return 0;
            else if (n == 1) return 1;
            else return fibonacci(n - 1) + fibonacci(n - 2);
        }
        
        main: function void() {
            fib: integer;
            fib = fibonacci(7);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    def test52(self):
        input = """
        gcd: function integer(a: integer, b: integer) {
            if (b == 0) return a;
            else return gcd(b, a % b);
        }
        
        main: function void() {
            res: integer;
            res = gcd(48, 18);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test53(self):
        input = """
        pow: function integer(base: integer, exp: integer) {
            if (exp == 0) return 1;
            else return base * pow(base, exp - 1);
        }
        
        main: function void() {
            result: integer;
            result = pow(2, 10);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    def test54(self):
        input = """
        sumArray: function integer(arr: array[5] of integer, n: integer) {
            if (n == 0) return arr[0];
            else return arr[n] + sumArray(arr, n - 1);
        }
        
        main: function void() {
            arr: array[5] of integer = {1, 2, 3, 4, 5};
            total: integer;
            total = sumArray(arr, 4);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test55(self):
        input = """

        
        main: function void() {
            str: string = "hello";
            rev: string;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test56(self):
        input = """
        main: function void() {
            a: integer = 5;
            b: integer = a + 10;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test57(self):
        input = """
        main: function void() {
            x: float = 3.14;
            y: float = x * 2.0;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test58(self):
        input = """
        main: function void() {
            s: string = "Hello";
            t: string = s :: " World";
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test59(self):
        input = """
        main: function void() {
            arr: array[3] of integer = {1, 2, 3};
            x: integer = arr[1];
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test60(self):
        input = """
        main: function void() {
            flag: boolean = true;
            if (flag) {
                flag = false;
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test61(self):
        input = """
        main: function void() {
            x: integer = 10;
            {
                y: integer = 20;
                x = x + y;
            }
            z: integer = x * 2;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test62(self):
        input = """
        main: function void() {
            x: integer = 5;
            if (x < 10) {
                x = x + 1;
            } else {
                y: integer = 20;
                y = y + 1;
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    def test63(self):
        input = """
        main: function void() {
            {
                a: integer = 10;
                {
                    b: integer = 20;
                    a = a + b;
                }
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test64(self):
        input = """
        main: function void() {
            a: integer = 10;
            {
                a: integer = 20;
                a = a + 1;
            }
            a = a + 1;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test65(self):
        input = """
        main: function void() {
            x: integer = 10;
            {
                y: integer = 20;
                {
                    z: integer = 30;
                    y = y + z;
                }
                x = x + y;
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 565))

    def test66(self):
        input = """
        baseFunc: function void() {
            printString("Base");
        }
        
        childFunc: function void() inherit baseFunc {
            super();
            printString("Child");
        }
        
        main: function void() {
            childFunc();
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 566))

    def test67(self):
        input = """
        baseFunc: function void() {
            printString("Hello");
        }
        
        greetFunc: function void() inherit baseFunc {
            super();
            printString("World");
        }
        
        main: function void() {
            greetFunc();
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 567))

    def test68(self):
        input = """
        baseFunc: function void() {
            printInteger(100);
        }
        
        doubleFunc: function void() inherit baseFunc {
            super();
            printInteger(200);
        }
        
        main: function void() {
            doubleFunc();
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 568))

    def test69(self):
        input = """
        rootFunc: function void() {
            writeFloat(3.14);
        }
        
        squareFunc: function void() inherit rootFunc {
            super();
            writeFloat(9.0);
        }
        
        main: function void() {
            squareFunc();
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 569))

    def test70(self):
        input = """
        parentFunc: function void() {
            printBoolean(true);
        }
        
        childFunc: function void() inherit parentFunc {
            super();
            printBoolean(false);
        }
        
        main: function void() {
            childFunc();
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 570))

    def test71(self):
        input = """
        add: function integer(a: integer, b: integer) {
            return a + b;
        }
        
        multiply: function integer(a: integer, b: integer) {
            return a * b;
        }
        
        main: function void() {
            x: integer;
            x = add(5, multiply(2, 3));
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 571))

    def test72(self):
        input = """
        baseFunc: function integer(a: integer, b: integer) {
            return a - b;
        }
        
        derivedFunc: function integer(a: integer, b: integer) inherit baseFunc {
            return super(a, b) * 2;
        }
        
        main: function void() {
            y: integer;
            y = derivedFunc(10, 3);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 572))

    def test73(self):
        input = """
        sum: function integer(a: integer, b: integer, c: integer) {
            return a + b + c;
        }
        
        product: function integer(a: integer, b: integer) {
            return a * b;
        }
        
        main: function void() {
            result: integer;
            result = sum(1, product(2, 3), 4);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 573))

    def test74(self):
        input = """
        factorial: function integer(n: integer) {
            if (n == 0) return 1;
            else return n * factorial(n - 1);
        }
        
        main: function void() {
            result: integer;
            result = factorial(4) + factorial(3);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 574))

    def test75(self):
        input = """
        isEven: function boolean(n: integer) {
            return n % 2 == 0;
        }
        
        isOdd: function boolean(n: integer) {
            return n % 2 != 0;
        }
        
        main: function void() {
            evenResult: boolean;
            oddResult: boolean;
            evenResult = isEven(4);
            oddResult = isOdd(7);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 575))

    def test76(self):
        input = """
        main: function void() {
            x: integer = 10;
            printInteger(x);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 576))

    def test77(self):
        input = """
        main: function void() {
            y: float = 3.14;
            writeFloat(y);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 577))

    def test78(self):
        input = """
        main: function void() {
            flag: boolean = true;
            printBoolean(flag);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 578))

    def test79(self):
        input = """
        main: function void() {
            message: string = "Hello, World!";
            printString(message);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 579))

    def test80(self):
        input = """
        main: function void() {
            num: integer;
            num = readInteger();
            printInteger(num);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 580))

    def test81(self):
        input = """
        main: function void() {
            x: integer;
            x = 10;
            y: integer = x;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    def test82(self):
        input = """
        main: function void() {
            a: float;
            a = 2.5;
            b: float = a * 2.0;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 582))

    def test83(self):
        input = """
        main: function void() {
            p: boolean;
            p = true;
            q: boolean = p || false;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 583))

    def test84(self):
        input = """
        main: function void() {
            s: string;
            s = "abc";
            t: string = s :: "def";
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 584))

    def test85(self):
        input = """
        main: function void() {
            arr: array[3] of integer = {1, 2, 3};
            i: integer = arr[0];
            j: integer = arr[2];
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 585))

    def test86(self):
        input = """
        main: function void() {
            arr: array[5] of integer = {1, 2, 3, 4, 5};
            sum: integer = 0;
            i: integer;
            for (i = 0, i < 5, i + 1) {
                sum = sum + arr[i];
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 586))

    def test87(self):
        input = """
        main: function void() {
            arr: array[3] of float = {1.1, 2.2, 3.3};
            product: float = 1.0;
            i: integer;
            for (i = 0, i < 3, i + 1) {
                product = product * arr[i];
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 587))

    def test88(self):
        input = """
        main: function void() {
            arr: array[4] of boolean = {true, false, true, false};
            result: boolean = true;
            i: integer;
            for (i = 0, i < 4, i + 1) {
                result = result && arr[i];
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 588))

    def test89(self):
        input = """
        main: function void() {
            arr: array[2] of string = {"hello", "world"};
            concat: string = "";
            i: integer;
            for (i = 0, i < 2, i + 1) {
                concat = concat :: arr[i];
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 589))

    def test90(self):
        input = """
        main: function void() {
            arr: array[3, 2] of integer = {{1, 2}, {3, 4}, {5, 6}};
            sum: integer = 0;
            i: integer;
            j: integer;
            for (i = 0, i < 3, i + 1) {
                for (j = 0, j < 2, j + 1) {
                    sum = sum + arr[i, j];
                }
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 590))

    def test91(self):
        input = """
        main: function void() {
            s1: string = "abc";
            s2: string = "def";
            s3: string = s1 :: s2;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 591))

    def test92(self):
        input = """
        main: function void() {
            s1: string = "hello";
            s2: string = " ";
            s3: string = "world";
            result: string = (s1 :: s2 ):: s3;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 592))

    def test93(self):
        input = """
        main: function void() {
            s: string = "abcdef";
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 593))

    def test94(self):
        input = """
        main: function void() {
            s: string = "123456";
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 594))

    def test95(self):
        input = """
        main: function void() {
            s: string = "abc";
            result: string = s :: "123";
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 595))

    def test96(self):
        input = """
        main: function void() {
            flag1: boolean = true;
            flag2: boolean = false;
            result: boolean = flag1 && flag2;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 596))

    def test97(self):
        input = """
        main: function void() {
            flag: boolean = true;
            result: boolean = !flag;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 597))

    def test98(self):
        input = """
        main: function void() {
            a: boolean = true;
            b: boolean = false;
            result: boolean = a || b;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 598))

    def test99(self):
        input = """
        main: function void() {
            x: integer = 10;
            y: integer = 20;
            result: boolean = x < y;
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 599))

    def test100(self):
        input = """
        main: function void() {
            a: boolean = true;
            b: boolean = false;
            result: boolean = (a && b) || (!b && a);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 600))
