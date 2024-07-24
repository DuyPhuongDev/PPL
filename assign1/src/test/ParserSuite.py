import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_1(self):
        input="""a: float;
                main: function void(a: float){
                    a = 1_234.567;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    
    def test_2(self):
        input="""a, b,c: integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    
    def test_3(self):
        input="""x, y: float = 1_23.2323, 232.0912;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    
    def test_4(self):
        input="""dental, pi , abc: interger;"""
        expect = "Error on line 1 col 18: interger"
        self.assertTrue(TestParser.test(input, expect, 204))
    
    def test_5(self):
        input="""str: string = "HELLO WORLD";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
    
    def test_6(self):
        input="""flag: boolean = TRUE;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))
    
    def test_7(self):
        input="""arr :array[2,5] of integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
    
    def test_8(self):
        input="""abc: void;"""
        expect = "Error on line 1 col 5: void"
        self.assertTrue(TestParser.test(input, expect, 208))
    
    def test_9(self):
        input="""it: auto = 1.23e+2;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))
    
    def test_10(self):
        input="""c: char;"""
        expect = "Error on line 1 col 3: char"
        self.assertTrue(TestParser.test(input, expect, 210))
    
    
    def test_11(self):
        input="""main: function void(argv: integer, args: array[5] of string){}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
    
    def test_12(self):
        input="""fibo: function integer(n: integer){}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))
    
    def test_13(self):
        input="""integer main(){}"""
        expect = "Error on line 1 col 0: integer"
        self.assertTrue(TestParser.test(input, expect, 213))
    
    def test_14(self):
        input="""animal: function string(){} """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))
    
    def test_15(self):
        input=  """
                    inc: function void (out x: float, incr: integer){
                        x = x + incr;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
    
    def test_16(self):
        input=  """
                    doctor: function void() inherit people{}
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
    
    def test_17(self):
        input=  """
                    BST: function (root: node){}
                """
        expect = "Error on line 2 col 34: ("
        self.assertTrue(TestParser.test(input, expect, 217))
    
    def test_18(self):
        input=  """
                    str: string = "hello world!";
                    main: function void(){
                       printString(str);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
    
    def test_19(self):
        input=  """
                    foo: function auto(a,b: integer){}
                """
        expect = "Error on line 2 col 40: ,"
        self.assertTrue(TestParser.test(input, expect, 219))
    
    def test_20(self):
        input=  """
                    main: function void() {
                    delta: integer = fact(3);
                    inc(x, delta);
                    printInteger(x);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))
        
    def test_21(self):
        input=  """
                    main: function void() {
                        id: integer;
                        id = 1_343_34;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))
    
    def test_22(self):
        input=  """
                    arr: array[5] of string;
                    main: function void(arr: array[5] of string) {
                        arr[0] = "hello";
                        arr[1] = "hi";
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
    
    def test_23(self):
        input=  """
                    main: function void() {
                        a: boolean;
                        a := 5;
                    }
                """
        expect = "Error on line 4 col 27: ="
        self.assertTrue(TestParser.test(input, expect, 223))
    
    def test_24(self):
        input=  """
                    main: function void() {
                        delta: integer = fact(3)
                    }
                """
        expect = "Error on line 4 col 20: }"
        self.assertTrue(TestParser.test(input, expect, 224))
    
    def test_25(self):
        input=  """
                    main: function void(str: string) {
                        str = "abc";
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
    
    def test_26(self):
        input=  """
                    main: function void(n: integer) {
                        str: string = "this is func";
                        if(n<5) printString(str);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
    
    def test_27(self):
        input=  """ a, b: integer;
                    main: function void(a: integer, b: integer) {
                        if(a!=b) preventDefault();
                        else return;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))
    
    def test_28(self):
        input=  """ a, b, c: integer;
                    max: function integer(a: integer, b: integer, c: integer) {
                        max: integer;
                        if((a>b) && (a>c)) max=a;
                        else {
                            if(b>c) max = b;
                            else max = c;
                        }
                        return max;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))
    
    def test_29(self):
        input=  """ week: function void(out x: string, n: integer){
                        if(n==2):
                            x = "Monday";
                        if(n==4):
                            x = "Webnesday";           
                    }
                """
        expect = "Error on line 2 col 32: :"
        self.assertTrue(TestParser.test(input, expect, 229))
    
    def test_30(self):
        input=  """ main: function void(){
                        if(TRUE) return;          
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))
        
    
    def test_31(self):
        input=  """ main: function void(){
                        i: integer;
                        for(i=0, i<10, i+1){
                            printInteger(i);
                        }          
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
        
    def test_32(self):
        input=  """ main: function void(){
                        for(i: integer = 1,i<10,i*2)  foo(abc);        
                    }
                """
        expect = "Error on line 2 col 29: :"
        self.assertTrue(TestParser.test(input, expect, 232))
        
    def test_33(self):
        input=  """ main: function void(){
                        count: integer = 0;
                        for(count, count!=10, count+2) preventDefault();          
                    }
                """
        expect = "Error on line 3 col 33: ,"
        self.assertTrue(TestParser.test(input, expect, 233))
        
    def test_34(self):
        input=  """ length: function integer(str: string){
                        length: integer=0;
                        for(i:auto=0;i<32;i+3){
                            length = length + i;
                        }           
                    }
                """
        expect = "Error on line 3 col 29: :"
        self.assertTrue(TestParser.test(input, expect, 234))
        
    def test_35(self):
        input=  """ main: function void(){
                        scala: int = 5;
                        for(scala, scala>0, scala-1){
                            printInteger(scala);
                        }        
                    }
                """
        expect = "Error on line 2 col 31: int"
        self.assertTrue(TestParser.test(input, expect, 235))
        
    def test_36(self):
        input=  """ main: function void(){
                        while(TRUE)
                            str="Hello world!";
                            printString(str); 
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))
        
    def test_37(self):
        input=  """ main: function void(){
                        count: integer = 10;
                        while(count>0){
                            printInteger(count);
                            count-1;   
                        }    
                    }
                """
        expect = "Error on line 5 col 33: -"
        self.assertTrue(TestParser.test(input, expect, 237))
        
    def test_38(self):
        input=  """ main: function void(){
                        while((x>y) && (x<z))
                            foo(abc);     
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))
        
    def test_39(self):
        input=  """ main: function void(){
                        while(FLASE):
                            i: float = 2.1;
                            writeFloat(i);      
                    }
                """
        expect = "Error on line 2 col 36: :"
        self.assertTrue(TestParser.test(input, expect, 239))
        
    def test_40(self):
        input=  """ main: function void(){
                        while(1)
                            sleep(2000);       
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))
        
    def test_41(self):
        input=  """ main: function void(){
                        while(isValid()) {
                            process();
                        }          
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))
    def test_42(self):
        input=  """ main: function void(){
                        if(TRUE)
                            if(FALSE) printString("false");
                            else printString("nested true");
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_43(self):
        input=  """ main: function void(){
                        if(FALSE) printString("false");
                        else if(TRUE) printString("true");
                        else printString("none");          
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_44(self):
        input=  """ main: function void(){
                        for(i: integer = 0, i < 10, i + 1) {
                            printInteger(i);
                        }          
                    }
                """
        expect = "Error on line 2 col 29: :"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_45(self):
        input=  """ main: function void(){
                        for(i = 0, i < 10; i + 1) {
                            printInteger(i);
                        }          
                    }
                """
        expect = "Error on line 2 col 41: ;"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_46(self):
        input=  """ main: function void(){
                        do {
                            printString("looping");
                        } while (FALSE);          
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_47(self):
        input=  """ main: function void(){
                        do {
                            printString("looping");
                        } FALSE;          
                    }
                """
        expect = "Error on line 4 col 26: FALSE"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_48(self):
        input=  """ main: function void(){
                        for(i = 0, i < 10) {
                            printInteger(i);
                        }          
                    }
                """
        expect = "Error on line 2 col 41: )"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_49(self):
        input=  """ main: function void(){
                        if(123) printString("invalid condition");         
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_50(self):
        input=  """ main: function void(){
                        if((abc!="abc") || (x == 5)) printString("OK");         
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
    
    def test_51(self):
        input=  """ main: function void(){
                        if(TRUE) {
                            if(FALSE) printString("false");
                            else printString("nested true");
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_52(self):
        input=  """ main: function void(){
                        a, b, c: integer;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_53(self):
        input=  """ foo: function integer(a: integer, b: integer) {
                        return a + b;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_54(self):
        input=  """ foo: function integer() {
                        return 1;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_55(self):
        input=  """ foo: function integer() {
                        return 1.0;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_56(self):
        input=  """ main: function void(){
                        while((a > b) && (b < c)) {
                            foo();
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_57(self):
        input=  """ main: function void(){
                        do {
                            foo();
                        } while (TRUE);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_58(self):
        input=  """ main: function void(){
                        a: integer = foo(1, 2) + bar(3, 4);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_59(self):
        input=  """ main: function void(){
                        a: integer = foo(1, 2;
                    }
                """
        expect = "Error on line 2 col 45: ;"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_60(self):
        input=  """ main: function void(){
                        a: array [5] of integer;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_61(self):
        input=  """ main: function void(){
                        a: array [5] of integer = {1, 2, 3, 4, 5};
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_62(self):
        input=  """ main: function void(){
                        a: array [5] of integer = {1, 2, 3, 4, 5, 6};
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_63(self):
        input=  """ main: function void(){
                        a: array [5] of integer;
                        a[0] = 1;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_64(self):
        input=  """ main: function void(){
                        a: array [5] of integer;
                        a[5] = 1;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_65(self):
        input=  """ main: function void(){
                        foo: function void() {
                            bar: function void() {
                                printString("bar");
                            }
                        }
                    }
                """
        expect = "Error on line 2 col 29: function"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_66(self):
        input=  """ main: function void(){
                        foo: function void() {
                            bar();
                        }
                    }
                """
        expect = "Error on line 2 col 29: function"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_67(self):
        input=  """ main: function void(){
                        if((a > b) && (c < d) || (e == f)) {
                            printString("complex condition");
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_68(self):
        input=  """ main: function void(){
                        if(a > b) {
                            printString("missing closing brace");
                        
                    }
                """
        expect = "Error on line 6 col 16: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_69(self):
        input=  """ main: function void(){
                        while(TRUE) {
                            break;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_70(self):
        input=  """ main: function void(){
                        while(TRUE) {
                            continue;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_71(self):
        input=  """ main: function void(){
                        for(i = 0, i < 10, i + 1) {
                            break;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_72(self):
        input=  """ main: function void(){
                        for(i = 0, i < 10, i + 1) {
                            continue;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_73(self):
        input=  """ foo: function void() {
                        return;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_74(self):
        input=  """ foo: function integer() {
                        return 1;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_75(self):
        input=  """ foo: function float() {
                        return 1.0;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_76(self):
        input=  """ foo: function string() {
                        return "hello";
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_77(self):
        input=  """ foo: function boolean() {
                        return TRUE;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_78(self):
        input=  """ foo: function auto() {
                        return bar();
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_79(self):
        input=  """ foo: function integer() {
                        return "string";
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_80(self):
        input=  """ foo: function array [5] of integer() {
                        return {1, 2, 3, 4, 5};
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_81(self):
        input=  """ main: function void(){
                        foo(1, 2, 3);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_82(self):
        input=  """ main: function void(){
                        foo(1);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_83(self):
        input=  """ main: function void(){
                        foo(1, 2);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_84(self):
        input=  """ main: function void(){
                        a: integer = foo(1, 2) + bar(3, 4);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_85(self):
        input=  """ main: function void(){
                        if(foo(1, 2)) {
                            printString("function call in condition");
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_86(self):
        input=  """ main: function void(){
                        while(foo(1, 2)) {
                            printString("function call in condition");
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_87(self):
        input=  """ main: function void(){
                        for(i = foo(1, 2), i < 10, i + 1) {
                            printInteger(i);
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_88(self):
        input=  """ main: function void(){
                        do {
                            printString("function call in condition");
                        } while (foo(1, 2));
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_89(self):
        input=  """ main: function void(){
                        a: integer = foo(1, 2) * bar(3, 4) + baz(5, 6);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_90(self):
        input=  """ main: function integer(){
                        return foo(1, 2);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_91(self):
        input=  """ main: function void(){
                        foo(bar(baz(1, 2), 3), 4);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_92(self):
        input=  """ main: function void(){
                        foo(bar(baz(1, 2, 3), 4), 5);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_93(self):
        input=  """ main: function void(){
                        a: auto = foo(1, 2);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_94(self):
        input=  """ main: function void(){
                        a: array [5] of integer = foo();
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_95(self):
        input=  """ main: function void(){
                        a: boolean = foo();
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_96(self):
        input=  """ main: function void(){
                        a: string = foo();
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_97(self):
        input=  """ main: function void(){
                        a: float = foo();
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))
        
    def test_98(self):
        input=  """ main: function void(){
                        a: integer = foo();
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_99(self):
        input=  """ main: function void(){
                        foo();
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_100(self):
        input=  """ main: function void(){
                        foo(1, 2, 3, 4, 5);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))
        