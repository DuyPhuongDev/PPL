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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u01dc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%")
        buf.write("\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-")
        buf.write("\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\3\61\7\61\u0142")
        buf.write("\n\61\f\61\16\61\u0145\13\61\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\62\7\62\u014d\n\62\f\62\16\62\u0150\13\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\63\3\63\7\63\u0159\n\63\f\63\16\63\u015c")
        buf.write("\13\63\3\64\3\64\3\64\3\65\3\65\3\65\5\65\u0164\n\65\3")
        buf.write("\65\3\65\3\65\3\65\5\65\u016a\n\65\3\65\3\65\3\65\5\65")
        buf.write("\u016f\n\65\3\66\3\66\3\66\7\66\u0174\n\66\f\66\16\66")
        buf.write("\u0177\13\66\3\66\3\66\6\66\u017b\n\66\r\66\16\66\u017c")
        buf.write("\7\66\u017f\n\66\f\66\16\66\u0182\13\66\5\66\u0184\n\66")
        buf.write("\3\67\3\67\6\67\u0188\n\67\r\67\16\67\u0189\38\38\58\u018e")
        buf.write("\n8\38\68\u0191\n8\r8\168\u0192\39\39\59\u0197\n9\3:\3")
        buf.write(":\7:\u019b\n:\f:\16:\u019e\13:\3:\3:\3:\3;\3;\3;\3;\5")
        buf.write(";\u01a7\n;\3<\3<\3<\3=\3=\3=\3=\7=\u01b0\n=\f=\16=\u01b3")
        buf.write("\13=\3=\3=\3>\3>\3>\3>\5>\u01bb\n>\3?\6?\u01be\n?\r?\16")
        buf.write("?\u01bf\3?\3?\3@\3@\7@\u01c6\n@\f@\16@\u01c9\13@\3@\3")
        buf.write("@\3A\3A\7A\u01cf\nA\fA\16A\u01d2\13A\3A\3A\3A\3B\3B\3")
        buf.write("B\3C\3C\3C\3\u014e\2D\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write("g\65i\66k\2m\2o\2q\67s8u\2w\2y9{\2}:\177;\u0081<\u0083")
        buf.write("\2\u0085=\3\2\22\3\2--\3\2//\3\2,,\3\2\61\61\3\2\'\'\3")
        buf.write("\2##\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3")
        buf.write("\2\62;\4\2GGgg\4\2--//\5\2\f\f\17\17$$\t\2))^^ddhhppt")
        buf.write("tvv\5\2\n\f\16\17\"\"\2\u01ec\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2q\3\2")
        buf.write("\2\2\2s\3\2\2\2\2y\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0081\3\2\2\2\2\u0085\3\2\2\2\3\u0087\3\2\2\2\5\u008c")
        buf.write("\3\2\2\2\7\u0092\3\2\2\2\t\u0097\3\2\2\2\13\u009f\3\2")
        buf.write("\2\2\r\u00a4\3\2\2\2\17\u00aa\3\2\2\2\21\u00b0\3\2\2\2")
        buf.write("\23\u00b6\3\2\2\2\25\u00bd\3\2\2\2\27\u00c1\3\2\2\2\31")
        buf.write("\u00c9\3\2\2\2\33\u00cd\3\2\2\2\35\u00d4\3\2\2\2\37\u00dd")
        buf.write("\3\2\2\2!\u00e0\3\2\2\2#\u00e9\3\2\2\2%\u00ec\3\2\2\2")
        buf.write("\'\u00f1\3\2\2\2)\u00f4\3\2\2\2+\u00fa\3\2\2\2-\u0102")
        buf.write("\3\2\2\2/\u0104\3\2\2\2\61\u0106\3\2\2\2\63\u0108\3\2")
        buf.write("\2\2\65\u010a\3\2\2\2\67\u010c\3\2\2\29\u010e\3\2\2\2")
        buf.write(";\u0111\3\2\2\2=\u0114\3\2\2\2?\u0117\3\2\2\2A\u011a\3")
        buf.write("\2\2\2C\u011c\3\2\2\2E\u011f\3\2\2\2G\u0121\3\2\2\2I\u0124")
        buf.write("\3\2\2\2K\u0127\3\2\2\2M\u0129\3\2\2\2O\u012b\3\2\2\2")
        buf.write("Q\u012d\3\2\2\2S\u012f\3\2\2\2U\u0131\3\2\2\2W\u0133\3")
        buf.write("\2\2\2Y\u0135\3\2\2\2[\u0137\3\2\2\2]\u0139\3\2\2\2_\u013b")
        buf.write("\3\2\2\2a\u013d\3\2\2\2c\u0148\3\2\2\2e\u0156\3\2\2\2")
        buf.write("g\u015d\3\2\2\2i\u016e\3\2\2\2k\u0183\3\2\2\2m\u0185\3")
        buf.write("\2\2\2o\u018b\3\2\2\2q\u0196\3\2\2\2s\u0198\3\2\2\2u\u01a6")
        buf.write("\3\2\2\2w\u01a8\3\2\2\2y\u01ab\3\2\2\2{\u01ba\3\2\2\2")
        buf.write("}\u01bd\3\2\2\2\177\u01c3\3\2\2\2\u0081\u01cc\3\2\2\2")
        buf.write("\u0083\u01d6\3\2\2\2\u0085\u01d9\3\2\2\2\u0087\u0088\7")
        buf.write("c\2\2\u0088\u0089\7w\2\2\u0089\u008a\7v\2\2\u008a\u008b")
        buf.write("\7q\2\2\u008b\4\3\2\2\2\u008c\u008d\7h\2\2\u008d\u008e")
        buf.write("\7c\2\2\u008e\u008f\7u\2\2\u008f\u0090\7n\2\2\u0090\u0091")
        buf.write("\7g\2\2\u0091\6\3\2\2\2\u0092\u0093\7v\2\2\u0093\u0094")
        buf.write("\7t\2\2\u0094\u0095\7w\2\2\u0095\u0096\7g\2\2\u0096\b")
        buf.write("\3\2\2\2\u0097\u0098\7k\2\2\u0098\u0099\7p\2\2\u0099\u009a")
        buf.write("\7v\2\2\u009a\u009b\7g\2\2\u009b\u009c\7i\2\2\u009c\u009d")
        buf.write("\7g\2\2\u009d\u009e\7t\2\2\u009e\n\3\2\2\2\u009f\u00a0")
        buf.write("\7x\2\2\u00a0\u00a1\7q\2\2\u00a1\u00a2\7k\2\2\u00a2\u00a3")
        buf.write("\7f\2\2\u00a3\f\3\2\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6")
        buf.write("\7t\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8\7c\2\2\u00a8\u00a9")
        buf.write("\7{\2\2\u00a9\16\3\2\2\2\u00aa\u00ab\7d\2\2\u00ab\u00ac")
        buf.write("\7t\2\2\u00ac\u00ad\7g\2\2\u00ad\u00ae\7c\2\2\u00ae\u00af")
        buf.write("\7m\2\2\u00af\20\3\2\2\2\u00b0\u00b1\7h\2\2\u00b1\u00b2")
        buf.write("\7n\2\2\u00b2\u00b3\7q\2\2\u00b3\u00b4\7c\2\2\u00b4\u00b5")
        buf.write("\7v\2\2\u00b5\22\3\2\2\2\u00b6\u00b7\7t\2\2\u00b7\u00b8")
        buf.write("\7g\2\2\u00b8\u00b9\7v\2\2\u00b9\u00ba\7w\2\2\u00ba\u00bb")
        buf.write("\7t\2\2\u00bb\u00bc\7p\2\2\u00bc\24\3\2\2\2\u00bd\u00be")
        buf.write("\7q\2\2\u00be\u00bf\7w\2\2\u00bf\u00c0\7v\2\2\u00c0\26")
        buf.write("\3\2\2\2\u00c1\u00c2\7d\2\2\u00c2\u00c3\7q\2\2\u00c3\u00c4")
        buf.write("\7q\2\2\u00c4\u00c5\7n\2\2\u00c5\u00c6\7g\2\2\u00c6\u00c7")
        buf.write("\7c\2\2\u00c7\u00c8\7p\2\2\u00c8\30\3\2\2\2\u00c9\u00ca")
        buf.write("\7h\2\2\u00ca\u00cb\7q\2\2\u00cb\u00cc\7t\2\2\u00cc\32")
        buf.write("\3\2\2\2\u00cd\u00ce\7u\2\2\u00ce\u00cf\7v\2\2\u00cf\u00d0")
        buf.write("\7t\2\2\u00d0\u00d1\7k\2\2\u00d1\u00d2\7p\2\2\u00d2\u00d3")
        buf.write("\7i\2\2\u00d3\34\3\2\2\2\u00d4\u00d5\7e\2\2\u00d5\u00d6")
        buf.write("\7q\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8\7v\2\2\u00d8\u00d9")
        buf.write("\7k\2\2\u00d9\u00da\7p\2\2\u00da\u00db\7w\2\2\u00db\u00dc")
        buf.write("\7g\2\2\u00dc\36\3\2\2\2\u00dd\u00de\7f\2\2\u00de\u00df")
        buf.write("\7q\2\2\u00df \3\2\2\2\u00e0\u00e1\7h\2\2\u00e1\u00e2")
        buf.write("\7w\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4\7e\2\2\u00e4\u00e5")
        buf.write("\7v\2\2\u00e5\u00e6\7k\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8")
        buf.write("\7p\2\2\u00e8\"\3\2\2\2\u00e9\u00ea\7q\2\2\u00ea\u00eb")
        buf.write("\7h\2\2\u00eb$\3\2\2\2\u00ec\u00ed\7g\2\2\u00ed\u00ee")
        buf.write("\7n\2\2\u00ee\u00ef\7u\2\2\u00ef\u00f0\7g\2\2\u00f0&\3")
        buf.write("\2\2\2\u00f1\u00f2\7k\2\2\u00f2\u00f3\7h\2\2\u00f3(\3")
        buf.write("\2\2\2\u00f4\u00f5\7y\2\2\u00f5\u00f6\7j\2\2\u00f6\u00f7")
        buf.write("\7k\2\2\u00f7\u00f8\7n\2\2\u00f8\u00f9\7g\2\2\u00f9*\3")
        buf.write("\2\2\2\u00fa\u00fb\7k\2\2\u00fb\u00fc\7p\2\2\u00fc\u00fd")
        buf.write("\7j\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100")
        buf.write("\7k\2\2\u0100\u0101\7v\2\2\u0101,\3\2\2\2\u0102\u0103")
        buf.write("\t\2\2\2\u0103.\3\2\2\2\u0104\u0105\t\3\2\2\u0105\60\3")
        buf.write("\2\2\2\u0106\u0107\t\4\2\2\u0107\62\3\2\2\2\u0108\u0109")
        buf.write("\t\5\2\2\u0109\64\3\2\2\2\u010a\u010b\t\6\2\2\u010b\66")
        buf.write("\3\2\2\2\u010c\u010d\t\7\2\2\u010d8\3\2\2\2\u010e\u010f")
        buf.write("\7(\2\2\u010f\u0110\7(\2\2\u0110:\3\2\2\2\u0111\u0112")
        buf.write("\7~\2\2\u0112\u0113\7~\2\2\u0113<\3\2\2\2\u0114\u0115")
        buf.write("\7?\2\2\u0115\u0116\7?\2\2\u0116>\3\2\2\2\u0117\u0118")
        buf.write("\7#\2\2\u0118\u0119\7?\2\2\u0119@\3\2\2\2\u011a\u011b")
        buf.write("\7>\2\2\u011bB\3\2\2\2\u011c\u011d\7>\2\2\u011d\u011e")
        buf.write("\7?\2\2\u011eD\3\2\2\2\u011f\u0120\7@\2\2\u0120F\3\2\2")
        buf.write("\2\u0121\u0122\7@\2\2\u0122\u0123\7?\2\2\u0123H\3\2\2")
        buf.write("\2\u0124\u0125\7<\2\2\u0125\u0126\7<\2\2\u0126J\3\2\2")
        buf.write("\2\u0127\u0128\7*\2\2\u0128L\3\2\2\2\u0129\u012a\7+\2")
        buf.write("\2\u012aN\3\2\2\2\u012b\u012c\7]\2\2\u012cP\3\2\2\2\u012d")
        buf.write("\u012e\7_\2\2\u012eR\3\2\2\2\u012f\u0130\7\60\2\2\u0130")
        buf.write("T\3\2\2\2\u0131\u0132\7.\2\2\u0132V\3\2\2\2\u0133\u0134")
        buf.write("\7=\2\2\u0134X\3\2\2\2\u0135\u0136\7<\2\2\u0136Z\3\2\2")
        buf.write("\2\u0137\u0138\7}\2\2\u0138\\\3\2\2\2\u0139\u013a\7\177")
        buf.write("\2\2\u013a^\3\2\2\2\u013b\u013c\7?\2\2\u013c`\3\2\2\2")
        buf.write("\u013d\u013e\7\61\2\2\u013e\u013f\7\61\2\2\u013f\u0143")
        buf.write("\3\2\2\2\u0140\u0142\n\b\2\2\u0141\u0140\3\2\2\2\u0142")
        buf.write("\u0145\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2")
        buf.write("\u0144\u0146\3\2\2\2\u0145\u0143\3\2\2\2\u0146\u0147\b")
        buf.write("\61\2\2\u0147b\3\2\2\2\u0148\u0149\7\61\2\2\u0149\u014a")
        buf.write("\7,\2\2\u014a\u014e\3\2\2\2\u014b\u014d\13\2\2\2\u014c")
        buf.write("\u014b\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014f\3\2\2\2")
        buf.write("\u014e\u014c\3\2\2\2\u014f\u0151\3\2\2\2\u0150\u014e\3")
        buf.write("\2\2\2\u0151\u0152\7,\2\2\u0152\u0153\7\61\2\2\u0153\u0154")
        buf.write("\3\2\2\2\u0154\u0155\b\62\2\2\u0155d\3\2\2\2\u0156\u015a")
        buf.write("\t\t\2\2\u0157\u0159\t\n\2\2\u0158\u0157\3\2\2\2\u0159")
        buf.write("\u015c\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2")
        buf.write("\u015bf\3\2\2\2\u015c\u015a\3\2\2\2\u015d\u015e\5k\66")
        buf.write("\2\u015e\u015f\b\64\3\2\u015fh\3\2\2\2\u0160\u0161\5k")
        buf.write("\66\2\u0161\u0163\5m\67\2\u0162\u0164\5o8\2\u0163\u0162")
        buf.write("\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165\3\2\2\2\u0165")
        buf.write("\u0166\b\65\4\2\u0166\u016f\3\2\2\2\u0167\u016a\5k\66")
        buf.write("\2\u0168\u016a\5m\67\2\u0169\u0167\3\2\2\2\u0169\u0168")
        buf.write("\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016c\5o8\2\u016c\u016d")
        buf.write("\b\65\5\2\u016d\u016f\3\2\2\2\u016e\u0160\3\2\2\2\u016e")
        buf.write("\u0169\3\2\2\2\u016fj\3\2\2\2\u0170\u0184\7\62\2\2\u0171")
        buf.write("\u0175\t\13\2\2\u0172\u0174\t\f\2\2\u0173\u0172\3\2\2")
        buf.write("\2\u0174\u0177\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176")
        buf.write("\3\2\2\2\u0176\u0180\3\2\2\2\u0177\u0175\3\2\2\2\u0178")
        buf.write("\u017a\7a\2\2\u0179\u017b\t\f\2\2\u017a\u0179\3\2\2\2")
        buf.write("\u017b\u017c\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d\3")
        buf.write("\2\2\2\u017d\u017f\3\2\2\2\u017e\u0178\3\2\2\2\u017f\u0182")
        buf.write("\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181")
        buf.write("\u0184\3\2\2\2\u0182\u0180\3\2\2\2\u0183\u0170\3\2\2\2")
        buf.write("\u0183\u0171\3\2\2\2\u0184l\3\2\2\2\u0185\u0187\5S*\2")
        buf.write("\u0186\u0188\t\f\2\2\u0187\u0186\3\2\2\2\u0188\u0189\3")
        buf.write("\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018an")
        buf.write("\3\2\2\2\u018b\u018d\t\r\2\2\u018c\u018e\t\16\2\2\u018d")
        buf.write("\u018c\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u0190\3\2\2\2")
        buf.write("\u018f\u0191\t\f\2\2\u0190\u018f\3\2\2\2\u0191\u0192\3")
        buf.write("\2\2\2\u0192\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193p")
        buf.write("\3\2\2\2\u0194\u0197\5\7\4\2\u0195\u0197\5\5\3\2\u0196")
        buf.write("\u0194\3\2\2\2\u0196\u0195\3\2\2\2\u0197r\3\2\2\2\u0198")
        buf.write("\u019c\7$\2\2\u0199\u019b\5u;\2\u019a\u0199\3\2\2\2\u019b")
        buf.write("\u019e\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d\3\2\2\2")
        buf.write("\u019d\u019f\3\2\2\2\u019e\u019c\3\2\2\2\u019f\u01a0\7")
        buf.write("$\2\2\u01a0\u01a1\b:\6\2\u01a1t\3\2\2\2\u01a2\u01a7\5")
        buf.write("w<\2\u01a3\u01a4\7^\2\2\u01a4\u01a7\7$\2\2\u01a5\u01a7")
        buf.write("\n\17\2\2\u01a6\u01a2\3\2\2\2\u01a6\u01a3\3\2\2\2\u01a6")
        buf.write("\u01a5\3\2\2\2\u01a7v\3\2\2\2\u01a8\u01a9\7^\2\2\u01a9")
        buf.write("\u01aa\t\20\2\2\u01aax\3\2\2\2\u01ab\u01ac\5[.\2\u01ac")
        buf.write("\u01b1\5{>\2\u01ad\u01ae\7.\2\2\u01ae\u01b0\5{>\2\u01af")
        buf.write("\u01ad\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2")
        buf.write("\u01b1\u01b2\3\2\2\2\u01b2\u01b4\3\2\2\2\u01b3\u01b1\3")
        buf.write("\2\2\2\u01b4\u01b5\5]/\2\u01b5z\3\2\2\2\u01b6\u01bb\5")
        buf.write("g\64\2\u01b7\u01bb\5i\65\2\u01b8\u01bb\5s:\2\u01b9\u01bb")
        buf.write("\5q9\2\u01ba\u01b6\3\2\2\2\u01ba\u01b7\3\2\2\2\u01ba\u01b8")
        buf.write("\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bb|\3\2\2\2\u01bc\u01be")
        buf.write("\t\21\2\2\u01bd\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf")
        buf.write("\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c1\3\2\2\2")
        buf.write("\u01c1\u01c2\b?\2\2\u01c2~\3\2\2\2\u01c3\u01c7\7$\2\2")
        buf.write("\u01c4\u01c6\5u;\2\u01c5\u01c4\3\2\2\2\u01c6\u01c9\3\2")
        buf.write("\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01ca")
        buf.write("\3\2\2\2\u01c9\u01c7\3\2\2\2\u01ca\u01cb\b@\7\2\u01cb")
        buf.write("\u0080\3\2\2\2\u01cc\u01d0\7$\2\2\u01cd\u01cf\5u;\2\u01ce")
        buf.write("\u01cd\3\2\2\2\u01cf\u01d2\3\2\2\2\u01d0\u01ce\3\2\2\2")
        buf.write("\u01d0\u01d1\3\2\2\2\u01d1\u01d3\3\2\2\2\u01d2\u01d0\3")
        buf.write("\2\2\2\u01d3\u01d4\5\u0083B\2\u01d4\u01d5\bA\b\2\u01d5")
        buf.write("\u0082\3\2\2\2\u01d6\u01d7\7^\2\2\u01d7\u01d8\n\20\2\2")
        buf.write("\u01d8\u0084\3\2\2\2\u01d9\u01da\13\2\2\2\u01da\u01db")
        buf.write("\bC\t\2\u01db\u0086\3\2\2\2\30\2\u0143\u014e\u015a\u0163")
        buf.write("\u0169\u016e\u0175\u017c\u0180\u0183\u0189\u018d\u0192")
        buf.write("\u0196\u019c\u01a6\u01b1\u01ba\u01bf\u01c7\u01d0\n\b\2")
        buf.write("\2\3\64\2\3\65\3\3\65\4\3:\5\3@\6\3A\7\3C\b")
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
    ARRLIT = 55
    WS = 56
    UNCLOSE_STRING = 57
    ILLEGAL_ESCAPE = 58
    ERROR_CHAR = 59

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
            "ARRLIT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
                  "ARRLIT", "ELEMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ILLESC", "ERROR_CHAR" ]

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
            actions[62] = self.UNCLOSE_STRING_action 
            actions[63] = self.ILLEGAL_ESCAPE_action 
            actions[65] = self.ERROR_CHAR_action 
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
     


