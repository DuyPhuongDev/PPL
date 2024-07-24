import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    # test comment
    def test_cmt_1(self):
        self.assertTrue(TestLexer.test("// This is inline cmt","<EOF>", 1))
    
    def test_cmt_2(self):
        self.assertTrue(TestLexer.test("a=5; // A C++ style comment","a,=,5,;,<EOF>", 2))
    
    def test_cmt_3(self):
        inp = """/* This is document cmt
                line 2adfsadsd
                line 3 sadjcv */ """
        out =  "<EOF>"
        self.assertTrue(TestLexer.test(inp, out, 3))
    
    # test indentifiers
    def test_iden_1(self):
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",4))
    
    def test_iden_2(self):
        self.assertTrue(TestLexer.test("_Ac9k_3sds","_Ac9k_3sds,<EOF>",5))
        
    def test_iden_3(self):
        self.assertTrue(TestLexer.test("aBc DeF gHi","aBc,DeF,gHi,<EOF>",6))
        
    def test_iden_4(self):
        self.assertTrue(TestLexer.test("int a = 5;","int,a,=,5,;,<EOF>",7))
        
    def test_iden_5(self):
        self.assertTrue(TestLexer.test("__aula","__aula,<EOF>",8))

    def test_iden_6(self):
        self.assertTrue(TestLexer.test("var1 var2 var3", "var1,var2,var3,<EOF>", 9))

    def test_iden_7(self):
        self.assertTrue(TestLexer.test("alpha beta gamma", "alpha,beta,gamma,<EOF>", 10))

    def test_iden_8(self):
        self.assertTrue(TestLexer.test("lex test case", "lex,test,case,<EOF>", 11))
    
    def test_error_token_1(self):
        self.assertTrue(TestLexer.test("@abc","Error Token @",12))
        
    def test_error_token_2(self):
        self.assertTrue(TestLexer.test("what?","what,Error Token ?",13))
        
    def test_error_token_3(self):
        self.assertTrue(TestLexer.test("foo $ bar", "foo,Error Token $", 14))

    def test_error_token_4(self):
        self.assertTrue(TestLexer.test("var1 & var2", "var1,Error Token &", 15))

    def test_error_token_5(self):
        self.assertTrue(TestLexer.test("alpha # beta", "alpha,Error Token #", 16))
    
    #test INTLIT
    def test_int_1(self):
        self.assertTrue(TestLexer.test('1234','1234,<EOF>',17))
    def test_int_2(self):
        self.assertTrue(TestLexer.test('1_234_567','1234567,<EOF>',18))
    def test_int_3(self):
        self.assertTrue(TestLexer.test('0','0,<EOF>',19))
    def test_int_4(self):
        self.assertTrue(TestLexer.test('453_3423','4533423,<EOF>',20))
    def test_int_5(self):
        self.assertTrue(TestLexer.test('9','9,<EOF>',21))
    
    # #test FloatLit
    def test_float_1(self):
        self.assertTrue(TestLexer.test('1.344','1.344,<EOF>',22))
    def test_float_2(self):
        self.assertTrue(TestLexer.test('2.23e10','2.23e10,<EOF>',23))
    def test_float_3(self):
        self.assertTrue(TestLexer.test('1_344.0','1344.0,<EOF>',24))
    def test_float_4(self):
        self.assertTrue(TestLexer.test('10E+20','10E+20,<EOF>',25))
    def test_float_5(self):
        self.assertTrue(TestLexer.test('10E-20','10E-20,<EOF>',26))
    def test_float_6(self):
        self.assertTrue(TestLexer.test('.05232e+10','.05232e+10,<EOF>',27))
    def test_float_7(self):
        self.assertTrue(TestLexer.test('6236_232.232E-12','6236232.232E-12,<EOF>',28))
    def test_float_8(self):
        self.assertTrue(TestLexer.test('1.0000000e-12','1.0000000e-12,<EOF>',29))
    def test_float_9(self):
        self.assertTrue(TestLexer.test('1_232_3232_23.02323','1232323223.02323,<EOF>',30))
    
    #bool lit
    def test_bool_1(self):
        self.assertTrue(TestLexer.test('true','true,<EOF>',31))
    def test_bool_2(self):
        self.assertTrue(TestLexer.test('false','false,<EOF>',32))
        
    # string lit
    def test_string_1(self):
        self.assertTrue(TestLexer.test(''' "Hello world!" ''', '''Hello world!,<EOF>''',33))        
    def test_string_2(self):
        self.assertTrue(TestLexer.test(''' "i'm wassana" ''', '''i'm wassana,<EOF>''',34))     
    def test_string_3(self):
        self.assertTrue(TestLexer.test(''' "She asked me: \\"Do you love me?\\"" ''', r'''She asked me: \"Do you love me?\",<EOF>''',35))
    def test_string_4(self):
        self.assertTrue(TestLexer.test(''' "I love you <3" ''', '''I love you <3,<EOF>''',36))
    def test_string_5(self):
        self.assertTrue(TestLexer.test(''' "This is a string." ''', '''This is a string.,<EOF>''',37))
    def test_string_6(self):
        self.assertTrue(TestLexer.test(r''' "This is a string with tab \t" ''', r'''This is a string with tab \t,<EOF>''',38))
    def test_string_7(self):
        self.assertTrue(TestLexer.test(''' "tab\t, single quote\', double quotes\\"" ''', r'''tab	, single quote', double quotes\",<EOF>''',39))
    def test_string_8(self):
        self.assertTrue(TestLexer.test(''' "Tdasd as324 ^$^" ''', '''Tdasd as324 ^$^,<EOF>''',40))
    def test_string_9(self):
        self.assertTrue(TestLexer.test(
            ''' "D:\\HCMUT\\HK233\\PPL\\BTL\\assign1\\src\\test\\LexerSuite.py" ''',
            r'''D:\HCMUT\HK233\PPL\BTL\assign1\src\test\LexerSuite.py,<EOF>''', 41
        ))
    def test_string_10(self):
        self.assertTrue(TestLexer.test(''' "This test is passed\r" ''', '''Unclosed String: This test is passed''',42))
    def test_string_11(self):
        self.assertTrue(TestLexer.test(''' "bow bow bow\n" ''', '''Unclosed String: bow bow bow''',43))
    def test_string_12(self):
        self.assertTrue(TestLexer.test(''' "today is wednesday''', '''Unclosed String: today is wednesday''',44))
    def test_string_13(self):
        self.assertTrue(TestLexer.test(r''' "illegal escape 1: \a"''', r'''illegal escape 1: \a,<EOF>''',45))
    def test_string_14(self):
        self.assertTrue(TestLexer.test(r''' "illegal escape 2: \f \b \t \e \c"''', r'''illegal escape 2: \f \b \t \e \c,<EOF>''',46))
    def test_string_15(self):
        self.assertTrue(TestLexer.test(r''' "illegal escape 3: \u \n \r"''', r'''illegal escape 3: \u \n \r,<EOF>''',47))
    def test_string_16(self):
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\"" """, r'''He asked me: \"Where is John?\",<EOF>''',48))
    def test_string_17(self):
        self.assertTrue(TestLexer.test(r''' "escape string \b \ \'" ''', r'''escape string \b \ \',<EOF>''',49))
    def test_string_18(self):
        self.assertTrue(TestLexer.test(r'''"a+11.2+\"mam.123\" 12 \"%^&"''', r'''a+11.2+\"mam.123\" 12 \"%^&,<EOF>''',50))

    # test combine
    def test_combine_1(self):
        inp = '''
            int i = 0;
            printf(i);
            '''
        out = '''int,i,=,0,;,printf,(,i,),;,<EOF>'''
        self.assertTrue(TestLexer.test(inp, out, 51))
        
    def test_combine_2(self):
        inp = ''' const pi = 3.14; '''
        out = '''const,pi,=,3.14,;,<EOF>'''
        self.assertTrue(TestLexer.test(inp, out, 52))
        
    def test_combine_3(self):
        inp = ''' str = "I love bach khoa" '''
        out = '''str,=,I love bach khoa,<EOF>'''
        self.assertTrue(TestLexer.test(inp, out, 53))
        
    def test_combine_4(self):
        inp = '''
                __str1 = "abc"
                __str2 = "def"
                __str1 + __str2 = "abcdef"
                '''
        out = '''__str1,=,abc,__str2,=,def,__str1,+,__str2,=,abcdef,<EOF>'''
        self.assertTrue(TestLexer.test(inp, out, 54))
        
    def test_combine_5(self):
        inp = ''' function handleClick(e){}'''
        out = '''function,handleClick,(,e,),{,},<EOF>'''
        self.assertTrue(TestLexer.test(inp, out, 55))
        
    def test_combine_6(self):
        inp = ''' int y = 5; // assign 5 to var y '''
        out = '''int,y,=,5,;,<EOF>'''
        self.assertTrue(TestLexer.test(inp, out, 56))
        
    def test_combine_7(self):
        inp = '''
            /* func to setCount
                input: none
                output: none
                */
                const [count, setCount] = useState(5);
                setCount(c => c+1);
                console.log(count);
            '''
        out = '''const,[,count,,,setCount,],=,useState,(,5,),;,setCount,(,c,=,>,c,+,1,),;,console,.,log,(,count,),;,<EOF>'''
        self.assertTrue(TestLexer.test(inp, out, 57))
        
    def test_combine_8(self):
        inp = ''' int y = 5; // assign 5 to var y '''
        out = '''int,y,=,5,;,<EOF>'''
        self.assertTrue(TestLexer.test(inp, out, 58))
        
    def test_combine_9(self):
        inp = ''' int y = 5; // assign 5 to var y '''
        out = '''int,y,=,5,;,<EOF>'''
        self.assertTrue(TestLexer.test(inp, out, 59))
        
    def test_combine_10(self):
        inp = ''' int y = 5; // assign 5 to var y '''
        out = '''int,y,=,5,;,<EOF>'''
        self.assertTrue(TestLexer.test(inp, out, 60))
        
    def test_1(self):
        self.assertTrue(TestLexer.test('acbsk^#^@&#$^(@)','acbsk,Error Token ^',61))
        
    def test_2(self):
        self.assertTrue(TestLexer.test('{1,2,3,4,5}',"{,1,,,2,,,3,,,4,,,5,},<EOF>",62))
        
    def test_3(self):
        self.assertTrue(TestLexer.test('3.14153465','3.14153465,<EOF>',63))
        
    def test_4(self):
        self.assertTrue(TestLexer.test('__var934AJFCDD JHJSD_WS121','__var934AJFCDD,JHJSD_WS121,<EOF>',64))
        
    def test_5(self):
        self.assertTrue(TestLexer.test('.0E+232','.0E+232,<EOF>',65))
        
    def test_6(self):
        self.assertTrue(TestLexer.test(r'''"i like PPL :)))) \b\b\b \t"''',r'''i like PPL :)))) \b\b\b \t,<EOF>''',66))
        
    def test_7(self):
        self.assertTrue(TestLexer.test(r''' "heloe leoeoanc \b\f''',r'''Unclosed String: heloe leoeoanc \b\f''',67))
        
    def test_8(self):
        self.assertTrue(TestLexer.test(r'''"what can i do?"''',r'''what can i do?,<EOF>''',68))
        
    def test_9(self):
        self.assertTrue(TestLexer.test("abc + -", "abc,+,-,<EOF>",69))
        
    def test_10(self):
        self.assertTrue(TestLexer.test("! == ^ & != && * % $ ... ","!,==,Error Token ^",70))
        
    def test_11(self):
        self.assertTrue(TestLexer.test(""" % erty == ! @ ksmdk ""","""%,erty,==,!,Error Token @""",71))
        
    def test_14(self):
        self.assertTrue(TestLexer.test("1320.3e+9 0.332e5","1320.3e+9,0.332e5,<EOF>",72))
        
    def test_15(self):
        inp = """vbnm"-a)
                    " """
        out = """vbnm,Unclosed String: -a)"""
        self.assertTrue(TestLexer.test(inp, out, 73))
        
    def test_16(self):
        self.assertTrue(TestLexer.test("adsaf!!!","adsaf,!,!,!,<EOF>",74))
        
    def test_17(self):
        self.assertTrue(TestLexer.test(""" {/*"*/*"}*/*""", """{,*,Unclosed String: }*/*""", 75))
        
    def test_18(self):
        self.assertTrue(TestLexer.test('"dphuongdev"', 'dphuongdev,<EOF>',76))
        
    def test_19(self):
        self.assertTrue(TestLexer.test('"Please give 10 point :)))"', 'Please give 10 point :))),<EOF>',77))
        
    def test_20(self):
        self.assertTrue(TestLexer.test('"i hate 0 point"', 'i hate 0 point,<EOF>',78))
        
    def test_21(self):
        input = """main: function void() {}"""
        expect = """main,:,function,void,(,),{,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 79))
    def test_22(self):
        input = """delta: integer = 3;"""
        expect = "delta,:,integer,=,3,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 80))
    
    def test_simple_5(self):
        input =   """x: integer = 65;
                    fact: function integer (n: integer){
                        if (n == 0) return 1;
                        else return n * fact(n - 1);
                    }
                    inc: function void(out n: integer,
                        delta: integer) {
                        n = n + delta;
                    }
                    main: function void() {
                        delta: integer = fact(3);
                        inc(x, delta);
                        printInteger(x);
                    }"""
        expect = "x,:,integer,=,65,;,fact,:,function,integer,(,n,:,integer,),{,if,(,n,==,0,),return,1,;,else,return,n,*,fact,(,n,-,1,),;,},inc,:,function,void,(,out,n,:,integer,,,delta,:,integer,),{,n,=,n,+,delta,;,},main,:,function,void,(,),{,delta,:,integer,=,fact,(,3,),;,inc,(,x,,,delta,),;,printInteger,(,x,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 81))
    
    def test_simple_6(self):
        input="""a: float;
                a = 4_212.12;"""
        expect = "a,:,float,;,a,=,4212.12,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 82))
        
    def test_23(self):
        self.assertTrue(TestLexer.test(r'''"Backslashes \\\\"''', r'''Backslashes \\\\,<EOF>''', 83))

    def test_24(self):
        self.assertTrue(TestLexer.test("0x123ABC", "0,x123ABC,<EOF>", 84))

    def test_25(self):
        self.assertTrue(TestLexer.test("0b101010", "0,b101010,<EOF>", 85))

    def test_26(self):
        self.assertTrue(TestLexer.test("0o1234567", "0,o1234567,<EOF>", 86))

    def test_27(self):
        self.assertTrue(TestLexer.test(r'''"String with tab\t"''', r'''String with tab\t,<EOF>''', 87))

    def test_28(self):
        self.assertTrue(TestLexer.test(r'''"String with newline\n"''', r'''String with newline\n,<EOF>''', 88))

    def test_29(self):
        self.assertTrue(TestLexer.test("5 + 10 == 15", "5,+,10,==,15,<EOF>", 89))

    def test_30(self):
        self.assertTrue(TestLexer.test("a && b || c", "a,&&,b,||,c,<EOF>", 90))

    def test_31(self):
        self.assertTrue(TestLexer.test("x << y >> z", "x,<,<,y,>,>,z,<EOF>", 91))

    def test_32(self):
        self.assertTrue(TestLexer.test("1.23e+10", "1.23e+10,<EOF>", 92))
        
    def test_33(self):
        self.assertTrue(TestLexer.test(r''' "Another unclosed string ''', r'''Unclosed String: Another unclosed string ''', 93))

    def test_34(self):
        self.assertTrue(TestLexer.test("123abc", "123,abc,<EOF>", 94))

    def test_35(self):
        self.assertTrue(TestLexer.test("1.2.3.4", "1.2,.,3.4,<EOF>", 95))

    def test_36(self):
        self.assertTrue(TestLexer.test("x = y + z;", "x,=,y,+,z,;,<EOF>", 96))

    def test_37(self):
        self.assertTrue(TestLexer.test("123 + 456 - 789 * 0", "123,+,456,-,789,*,0,<EOF>", 97))

    def test_38(self):
        self.assertTrue(TestLexer.test("func(a, b, c);", "func,(,a,,,b,,,c,),;,<EOF>", 98))

    def test_39(self):
        self.assertTrue(TestLexer.test("[1, 2, 3]", "[,1,,,2,,,3,],<EOF>", 99))

    def test_40(self):
        self.assertTrue(TestLexer.test("== != <= >=", "==,!=,<=,>=,<EOF>", 100))