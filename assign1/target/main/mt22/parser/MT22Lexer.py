# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01c7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\61\3\61\7\61\u013e\n\61\f\61\16\61")
        buf.write("\u0141\13\61\3\61\3\61\3\62\3\62\3\62\3\62\7\62\u0149")
        buf.write("\n\62\f\62\16\62\u014c\13\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\63\3\63\7\63\u0155\n\63\f\63\16\63\u0158\13\63\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\65\5\65\u0160\n\65\3\65\3\65\3")
        buf.write("\65\3\65\5\65\u0166\n\65\3\65\3\65\3\65\5\65\u016b\n\65")
        buf.write("\3\66\3\66\3\66\7\66\u0170\n\66\f\66\16\66\u0173\13\66")
        buf.write("\3\66\3\66\6\66\u0177\n\66\r\66\16\66\u0178\7\66\u017b")
        buf.write("\n\66\f\66\16\66\u017e\13\66\5\66\u0180\n\66\3\67\3\67")
        buf.write("\6\67\u0184\n\67\r\67\16\67\u0185\38\38\58\u018a\n8\3")
        buf.write("8\68\u018d\n8\r8\168\u018e\39\39\59\u0193\n9\3:\3:\7:")
        buf.write("\u0197\n:\f:\16:\u019a\13:\3:\3:\3:\3;\3;\3;\3;\5;\u01a3")
        buf.write("\n;\3<\3<\3<\3=\6=\u01a9\n=\r=\16=\u01aa\3=\3=\3>\3>\7")
        buf.write(">\u01b1\n>\f>\16>\u01b4\13>\3>\3>\3?\3?\7?\u01ba\n?\f")
        buf.write("?\16?\u01bd\13?\3?\3?\3?\3@\3@\3@\3A\3A\3A\3\u014a\2B")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\2m\2o\2q\67")
        buf.write("s8u\2w\2y9{:};\177\2\u0081<\3\2\22\3\2--\3\2//\3\2,,\3")
        buf.write("\2\61\61\3\2\'\'\3\2##\4\2\f\f\17\17\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\3\2\63;\3\2\62;\4\2GGgg\4\2--//\5\2\f\f\17\17")
        buf.write("$$\t\2))^^ddhhppttvv\5\2\n\f\16\17\"\"\2\u01d4\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\u0081\3\2\2\2\3\u0083\3\2\2\2\5\u0088\3")
        buf.write("\2\2\2\7\u008e\3\2\2\2\t\u0093\3\2\2\2\13\u009b\3\2\2")
        buf.write("\2\r\u00a0\3\2\2\2\17\u00a6\3\2\2\2\21\u00ac\3\2\2\2\23")
        buf.write("\u00b2\3\2\2\2\25\u00b9\3\2\2\2\27\u00bd\3\2\2\2\31\u00c5")
        buf.write("\3\2\2\2\33\u00c9\3\2\2\2\35\u00d0\3\2\2\2\37\u00d9\3")
        buf.write("\2\2\2!\u00dc\3\2\2\2#\u00e5\3\2\2\2%\u00e8\3\2\2\2\'")
        buf.write("\u00ed\3\2\2\2)\u00f0\3\2\2\2+\u00f6\3\2\2\2-\u00fe\3")
        buf.write("\2\2\2/\u0100\3\2\2\2\61\u0102\3\2\2\2\63\u0104\3\2\2")
        buf.write("\2\65\u0106\3\2\2\2\67\u0108\3\2\2\29\u010a\3\2\2\2;\u010d")
        buf.write("\3\2\2\2=\u0110\3\2\2\2?\u0113\3\2\2\2A\u0116\3\2\2\2")
        buf.write("C\u0118\3\2\2\2E\u011b\3\2\2\2G\u011d\3\2\2\2I\u0120\3")
        buf.write("\2\2\2K\u0123\3\2\2\2M\u0125\3\2\2\2O\u0127\3\2\2\2Q\u0129")
        buf.write("\3\2\2\2S\u012b\3\2\2\2U\u012d\3\2\2\2W\u012f\3\2\2\2")
        buf.write("Y\u0131\3\2\2\2[\u0133\3\2\2\2]\u0135\3\2\2\2_\u0137\3")
        buf.write("\2\2\2a\u0139\3\2\2\2c\u0144\3\2\2\2e\u0152\3\2\2\2g\u0159")
        buf.write("\3\2\2\2i\u016a\3\2\2\2k\u017f\3\2\2\2m\u0181\3\2\2\2")
        buf.write("o\u0187\3\2\2\2q\u0192\3\2\2\2s\u0194\3\2\2\2u\u01a2\3")
        buf.write("\2\2\2w\u01a4\3\2\2\2y\u01a8\3\2\2\2{\u01ae\3\2\2\2}\u01b7")
        buf.write("\3\2\2\2\177\u01c1\3\2\2\2\u0081\u01c4\3\2\2\2\u0083\u0084")
        buf.write("\7c\2\2\u0084\u0085\7w\2\2\u0085\u0086\7v\2\2\u0086\u0087")
        buf.write("\7q\2\2\u0087\4\3\2\2\2\u0088\u0089\7h\2\2\u0089\u008a")
        buf.write("\7c\2\2\u008a\u008b\7u\2\2\u008b\u008c\7n\2\2\u008c\u008d")
        buf.write("\7g\2\2\u008d\6\3\2\2\2\u008e\u008f\7v\2\2\u008f\u0090")
        buf.write("\7t\2\2\u0090\u0091\7w\2\2\u0091\u0092\7g\2\2\u0092\b")
        buf.write("\3\2\2\2\u0093\u0094\7k\2\2\u0094\u0095\7p\2\2\u0095\u0096")
        buf.write("\7v\2\2\u0096\u0097\7g\2\2\u0097\u0098\7i\2\2\u0098\u0099")
        buf.write("\7g\2\2\u0099\u009a\7t\2\2\u009a\n\3\2\2\2\u009b\u009c")
        buf.write("\7x\2\2\u009c\u009d\7q\2\2\u009d\u009e\7k\2\2\u009e\u009f")
        buf.write("\7f\2\2\u009f\f\3\2\2\2\u00a0\u00a1\7c\2\2\u00a1\u00a2")
        buf.write("\7t\2\2\u00a2\u00a3\7t\2\2\u00a3\u00a4\7c\2\2\u00a4\u00a5")
        buf.write("\7{\2\2\u00a5\16\3\2\2\2\u00a6\u00a7\7d\2\2\u00a7\u00a8")
        buf.write("\7t\2\2\u00a8\u00a9\7g\2\2\u00a9\u00aa\7c\2\2\u00aa\u00ab")
        buf.write("\7m\2\2\u00ab\20\3\2\2\2\u00ac\u00ad\7h\2\2\u00ad\u00ae")
        buf.write("\7n\2\2\u00ae\u00af\7q\2\2\u00af\u00b0\7c\2\2\u00b0\u00b1")
        buf.write("\7v\2\2\u00b1\22\3\2\2\2\u00b2\u00b3\7t\2\2\u00b3\u00b4")
        buf.write("\7g\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6\7w\2\2\u00b6\u00b7")
        buf.write("\7t\2\2\u00b7\u00b8\7p\2\2\u00b8\24\3\2\2\2\u00b9\u00ba")
        buf.write("\7q\2\2\u00ba\u00bb\7w\2\2\u00bb\u00bc\7v\2\2\u00bc\26")
        buf.write("\3\2\2\2\u00bd\u00be\7d\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0")
        buf.write("\7q\2\2\u00c0\u00c1\7n\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3")
        buf.write("\7c\2\2\u00c3\u00c4\7p\2\2\u00c4\30\3\2\2\2\u00c5\u00c6")
        buf.write("\7h\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8\7t\2\2\u00c8\32")
        buf.write("\3\2\2\2\u00c9\u00ca\7u\2\2\u00ca\u00cb\7v\2\2\u00cb\u00cc")
        buf.write("\7t\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce\7p\2\2\u00ce\u00cf")
        buf.write("\7i\2\2\u00cf\34\3\2\2\2\u00d0\u00d1\7e\2\2\u00d1\u00d2")
        buf.write("\7q\2\2\u00d2\u00d3\7p\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5")
        buf.write("\7k\2\2\u00d5\u00d6\7p\2\2\u00d6\u00d7\7w\2\2\u00d7\u00d8")
        buf.write("\7g\2\2\u00d8\36\3\2\2\2\u00d9\u00da\7f\2\2\u00da\u00db")
        buf.write("\7q\2\2\u00db \3\2\2\2\u00dc\u00dd\7h\2\2\u00dd\u00de")
        buf.write("\7w\2\2\u00de\u00df\7p\2\2\u00df\u00e0\7e\2\2\u00e0\u00e1")
        buf.write("\7v\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4")
        buf.write("\7p\2\2\u00e4\"\3\2\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7")
        buf.write("\7h\2\2\u00e7$\3\2\2\2\u00e8\u00e9\7g\2\2\u00e9\u00ea")
        buf.write("\7n\2\2\u00ea\u00eb\7u\2\2\u00eb\u00ec\7g\2\2\u00ec&\3")
        buf.write("\2\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef\7h\2\2\u00ef(\3")
        buf.write("\2\2\2\u00f0\u00f1\7y\2\2\u00f1\u00f2\7j\2\2\u00f2\u00f3")
        buf.write("\7k\2\2\u00f3\u00f4\7n\2\2\u00f4\u00f5\7g\2\2\u00f5*\3")
        buf.write("\2\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9")
        buf.write("\7j\2\2\u00f9\u00fa\7g\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc")
        buf.write("\7k\2\2\u00fc\u00fd\7v\2\2\u00fd,\3\2\2\2\u00fe\u00ff")
        buf.write("\t\2\2\2\u00ff.\3\2\2\2\u0100\u0101\t\3\2\2\u0101\60\3")
        buf.write("\2\2\2\u0102\u0103\t\4\2\2\u0103\62\3\2\2\2\u0104\u0105")
        buf.write("\t\5\2\2\u0105\64\3\2\2\2\u0106\u0107\t\6\2\2\u0107\66")
        buf.write("\3\2\2\2\u0108\u0109\t\7\2\2\u01098\3\2\2\2\u010a\u010b")
        buf.write("\7(\2\2\u010b\u010c\7(\2\2\u010c:\3\2\2\2\u010d\u010e")
        buf.write("\7~\2\2\u010e\u010f\7~\2\2\u010f<\3\2\2\2\u0110\u0111")
        buf.write("\7?\2\2\u0111\u0112\7?\2\2\u0112>\3\2\2\2\u0113\u0114")
        buf.write("\7#\2\2\u0114\u0115\7?\2\2\u0115@\3\2\2\2\u0116\u0117")
        buf.write("\7>\2\2\u0117B\3\2\2\2\u0118\u0119\7>\2\2\u0119\u011a")
        buf.write("\7?\2\2\u011aD\3\2\2\2\u011b\u011c\7@\2\2\u011cF\3\2\2")
        buf.write("\2\u011d\u011e\7@\2\2\u011e\u011f\7?\2\2\u011fH\3\2\2")
        buf.write("\2\u0120\u0121\7<\2\2\u0121\u0122\7<\2\2\u0122J\3\2\2")
        buf.write("\2\u0123\u0124\7*\2\2\u0124L\3\2\2\2\u0125\u0126\7+\2")
        buf.write("\2\u0126N\3\2\2\2\u0127\u0128\7]\2\2\u0128P\3\2\2\2\u0129")
        buf.write("\u012a\7_\2\2\u012aR\3\2\2\2\u012b\u012c\7\60\2\2\u012c")
        buf.write("T\3\2\2\2\u012d\u012e\7.\2\2\u012eV\3\2\2\2\u012f\u0130")
        buf.write("\7=\2\2\u0130X\3\2\2\2\u0131\u0132\7<\2\2\u0132Z\3\2\2")
        buf.write("\2\u0133\u0134\7}\2\2\u0134\\\3\2\2\2\u0135\u0136\7\177")
        buf.write("\2\2\u0136^\3\2\2\2\u0137\u0138\7?\2\2\u0138`\3\2\2\2")
        buf.write("\u0139\u013a\7\61\2\2\u013a\u013b\7\61\2\2\u013b\u013f")
        buf.write("\3\2\2\2\u013c\u013e\n\b\2\2\u013d\u013c\3\2\2\2\u013e")
        buf.write("\u0141\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140\3\2\2\2")
        buf.write("\u0140\u0142\3\2\2\2\u0141\u013f\3\2\2\2\u0142\u0143\b")
        buf.write("\61\2\2\u0143b\3\2\2\2\u0144\u0145\7\61\2\2\u0145\u0146")
        buf.write("\7,\2\2\u0146\u014a\3\2\2\2\u0147\u0149\13\2\2\2\u0148")
        buf.write("\u0147\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u014b\3\2\2\2")
        buf.write("\u014a\u0148\3\2\2\2\u014b\u014d\3\2\2\2\u014c\u014a\3")
        buf.write("\2\2\2\u014d\u014e\7,\2\2\u014e\u014f\7\61\2\2\u014f\u0150")
        buf.write("\3\2\2\2\u0150\u0151\b\62\2\2\u0151d\3\2\2\2\u0152\u0156")
        buf.write("\t\t\2\2\u0153\u0155\t\n\2\2\u0154\u0153\3\2\2\2\u0155")
        buf.write("\u0158\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0157\3\2\2\2")
        buf.write("\u0157f\3\2\2\2\u0158\u0156\3\2\2\2\u0159\u015a\5k\66")
        buf.write("\2\u015a\u015b\b\64\3\2\u015bh\3\2\2\2\u015c\u015d\5k")
        buf.write("\66\2\u015d\u015f\5m\67\2\u015e\u0160\5o8\2\u015f\u015e")
        buf.write("\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0161\3\2\2\2\u0161")
        buf.write("\u0162\b\65\4\2\u0162\u016b\3\2\2\2\u0163\u0166\5k\66")
        buf.write("\2\u0164\u0166\5m\67\2\u0165\u0163\3\2\2\2\u0165\u0164")
        buf.write("\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0168\5o8\2\u0168\u0169")
        buf.write("\b\65\5\2\u0169\u016b\3\2\2\2\u016a\u015c\3\2\2\2\u016a")
        buf.write("\u0165\3\2\2\2\u016bj\3\2\2\2\u016c\u0180\7\62\2\2\u016d")
        buf.write("\u0171\t\13\2\2\u016e\u0170\t\f\2\2\u016f\u016e\3\2\2")
        buf.write("\2\u0170\u0173\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0172")
        buf.write("\3\2\2\2\u0172\u017c\3\2\2\2\u0173\u0171\3\2\2\2\u0174")
        buf.write("\u0176\7a\2\2\u0175\u0177\t\f\2\2\u0176\u0175\3\2\2\2")
        buf.write("\u0177\u0178\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3")
        buf.write("\2\2\2\u0179\u017b\3\2\2\2\u017a\u0174\3\2\2\2\u017b\u017e")
        buf.write("\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017d")
        buf.write("\u0180\3\2\2\2\u017e\u017c\3\2\2\2\u017f\u016c\3\2\2\2")
        buf.write("\u017f\u016d\3\2\2\2\u0180l\3\2\2\2\u0181\u0183\5S*\2")
        buf.write("\u0182\u0184\t\f\2\2\u0183\u0182\3\2\2\2\u0184\u0185\3")
        buf.write("\2\2\2\u0185\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186n")
        buf.write("\3\2\2\2\u0187\u0189\t\r\2\2\u0188\u018a\t\16\2\2\u0189")
        buf.write("\u0188\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018c\3\2\2\2")
        buf.write("\u018b\u018d\t\f\2\2\u018c\u018b\3\2\2\2\u018d\u018e\3")
        buf.write("\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018fp")
        buf.write("\3\2\2\2\u0190\u0193\5\7\4\2\u0191\u0193\5\5\3\2\u0192")
        buf.write("\u0190\3\2\2\2\u0192\u0191\3\2\2\2\u0193r\3\2\2\2\u0194")
        buf.write("\u0198\7$\2\2\u0195\u0197\5u;\2\u0196\u0195\3\2\2\2\u0197")
        buf.write("\u019a\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0199\3\2\2\2")
        buf.write("\u0199\u019b\3\2\2\2\u019a\u0198\3\2\2\2\u019b\u019c\7")
        buf.write("$\2\2\u019c\u019d\b:\6\2\u019dt\3\2\2\2\u019e\u01a3\5")
        buf.write("w<\2\u019f\u01a0\7^\2\2\u01a0\u01a3\7$\2\2\u01a1\u01a3")
        buf.write("\n\17\2\2\u01a2\u019e\3\2\2\2\u01a2\u019f\3\2\2\2\u01a2")
        buf.write("\u01a1\3\2\2\2\u01a3v\3\2\2\2\u01a4\u01a5\7^\2\2\u01a5")
        buf.write("\u01a6\t\20\2\2\u01a6x\3\2\2\2\u01a7\u01a9\t\21\2\2\u01a8")
        buf.write("\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01a8\3\2\2\2")
        buf.write("\u01aa\u01ab\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ad\b")
        buf.write("=\2\2\u01adz\3\2\2\2\u01ae\u01b2\7$\2\2\u01af\u01b1\5")
        buf.write("u;\2\u01b0\u01af\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0")
        buf.write("\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b5\3\2\2\2\u01b4")
        buf.write("\u01b2\3\2\2\2\u01b5\u01b6\b>\7\2\u01b6|\3\2\2\2\u01b7")
        buf.write("\u01bb\7$\2\2\u01b8\u01ba\5u;\2\u01b9\u01b8\3\2\2\2\u01ba")
        buf.write("\u01bd\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2")
        buf.write("\u01bc\u01be\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be\u01bf\5")
        buf.write("\177@\2\u01bf\u01c0\b?\b\2\u01c0~\3\2\2\2\u01c1\u01c2")
        buf.write("\7^\2\2\u01c2\u01c3\n\20\2\2\u01c3\u0080\3\2\2\2\u01c4")
        buf.write("\u01c5\13\2\2\2\u01c5\u01c6\bA\t\2\u01c6\u0082\3\2\2\2")
        buf.write("\26\2\u013f\u014a\u0156\u015f\u0165\u016a\u0171\u0178")
        buf.write("\u017c\u017f\u0185\u0189\u018e\u0192\u0198\u01a2\u01aa")
        buf.write("\u01b2\u01bb\n\b\2\2\3\64\2\3\65\3\3\65\4\3:\5\3>\6\3")
        buf.write("?\7\3A\b")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    FALSE = 2
    TRUE = 3
    INTEGER = 4
    VOID = 5
    ARRAY = 6
    BREAK = 7
    FLOAT = 8
    RETURN = 9
    OUT = 10
    BOOLEAN = 11
    FOR = 12
    STRING = 13
    CONTINUE = 14
    DO = 15
    FUNCTION = 16
    OF = 17
    ELSE = 18
    IF = 19
    WHILE = 20
    INHERIT = 21
    PLUS = 22
    MINUS = 23
    MUL = 24
    DIV = 25
    MOD = 26
    NOT = 27
    AND = 28
    OR = 29
    EQUAL = 30
    NOTEQUAL = 31
    LESS = 32
    LESSEQUAL = 33
    GREATER = 34
    GREATEREQUAL = 35
    DBCOLON = 36
    LROUNDBR = 37
    RROUNDBR = 38
    LSQUAREBR = 39
    RSQUAREBR = 40
    DOT = 41
    COMMA = 42
    SEMI_COLON = 43
    COLON = 44
    LBRACES = 45
    RBRACES = 46
    ASSIGN = 47
    CPP_CMT = 48
    C_CMT = 49
    IDENTIFIERS = 50
    INTLIT = 51
    FLOATLIT = 52
    BOOLEANLIT = 53
    STRINGLIT = 54
    WS = 55
    UNCLOSE_STRING = 56
    ILLEGAL_ESCAPE = 57
    ERROR_CHAR = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'fasle'", "'true'", "'integer'", "'void'", "'array'", 
            "'break'", "'float'", "'return'", "'out'", "'boolean'", "'for'", 
            "'string'", "'continue'", "'do'", "'function'", "'of'", "'else'", 
            "'if'", "'while'", "'inherit'", "'&&'", "'||'", "'=='", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'::'", "'('", "')'", "'['", "']'", 
            "'.'", "','", "';'", "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "FALSE", "TRUE", "INTEGER", "VOID", "ARRAY", "BREAK", 
            "FLOAT", "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", 
            "DO", "FUNCTION", "OF", "ELSE", "IF", "WHILE", "INHERIT", "PLUS", 
            "MINUS", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "NOTEQUAL", 
            "LESS", "LESSEQUAL", "GREATER", "GREATEREQUAL", "DBCOLON", "LROUNDBR", 
            "RROUNDBR", "LSQUAREBR", "RSQUAREBR", "DOT", "COMMA", "SEMI_COLON", 
            "COLON", "LBRACES", "RBRACES", "ASSIGN", "CPP_CMT", "C_CMT", 
            "IDENTIFIERS", "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "AUTO", "FALSE", "TRUE", "INTEGER", "VOID", "ARRAY", "BREAK", 
                  "FLOAT", "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", 
                  "CONTINUE", "DO", "FUNCTION", "OF", "ELSE", "IF", "WHILE", 
                  "INHERIT", "PLUS", "MINUS", "MUL", "DIV", "MOD", "NOT", 
                  "AND", "OR", "EQUAL", "NOTEQUAL", "LESS", "LESSEQUAL", 
                  "GREATER", "GREATEREQUAL", "DBCOLON", "LROUNDBR", "RROUNDBR", 
                  "LSQUAREBR", "RSQUAREBR", "DOT", "COMMA", "SEMI_COLON", 
                  "COLON", "LBRACES", "RBRACES", "ASSIGN", "CPP_CMT", "C_CMT", 
                  "IDENTIFIERS", "INTLIT", "FLOATLIT", "POSITIVE", "DECIMAl", 
                  "EXPONENT", "BOOLEANLIT", "STRINGLIT", "STR_CHAR", "ESC_SEQ", 
                  "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ILLESC", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[50] = self.INTLIT_action 
            actions[51] = self.FLOATLIT_action 
            actions[56] = self.STRINGLIT_action 
            actions[60] = self.UNCLOSE_STRING_action 
            actions[61] = self.ILLEGAL_ESCAPE_action 
            actions[63] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_","")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_","")
     

        if actionIndex == 2:
            self.text = self.text.replace("_","")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            				raise IllegalEscape(self.text[1:]);
            			
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise ErrorToken(self.text)
     


