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
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3")
        buf.write("%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3")
        buf.write("-\3.\3.\3/\3/\3/\3/\7/\u0133\n/\f/\16/\u0136\13/\3/\3")
        buf.write("/\3\60\3\60\3\60\3\60\7\60\u013e\n\60\f\60\16\60\u0141")
        buf.write("\13\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\5\61\u014a\n")
        buf.write("\61\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\64\3\64\7\64\u0159\n\64\f\64\16\64\u015c\13\64")
        buf.write("\3\65\3\65\3\65\3\66\3\66\3\66\5\66\u0164\n\66\3\66\3")
        buf.write("\66\3\66\3\66\5\66\u016a\n\66\3\66\3\66\3\66\5\66\u016f")
        buf.write("\n\66\3\67\3\67\3\67\7\67\u0174\n\67\f\67\16\67\u0177")
        buf.write("\13\67\3\67\3\67\6\67\u017b\n\67\r\67\16\67\u017c\7\67")
        buf.write("\u017f\n\67\f\67\16\67\u0182\13\67\5\67\u0184\n\67\38")
        buf.write("\38\68\u0188\n8\r8\168\u0189\39\39\59\u018e\n9\39\69\u0191")
        buf.write("\n9\r9\169\u0192\3:\3:\7:\u0197\n:\f:\16:\u019a\13:\3")
        buf.write(":\3:\3:\3;\3;\3;\3;\5;\u01a3\n;\3<\3<\3<\3=\6=\u01a9\n")
        buf.write("=\r=\16=\u01aa\3=\3=\3>\3>\7>\u01b1\n>\f>\16>\u01b4\13")
        buf.write(">\3>\3>\3?\3?\7?\u01ba\n?\f?\16?\u01bd\13?\3?\3?\3?\3")
        buf.write("@\3@\3@\3A\3A\3A\3\u013f\2B\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m\2o\2q\2s8u\2w\2y9{:};\177\2\u0081<\3")
        buf.write("\2\22\3\2--\3\2//\3\2,,\3\2\61\61\3\2\'\'\3\2##\4\2\f")
        buf.write("\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4\2")
        buf.write("GGgg\4\2--//\5\2\f\f\17\17$$\t\2))^^ddhhppttvv\5\2\n\f")
        buf.write("\16\17\"\"\2\u01d4\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2s\3\2\2")
        buf.write("\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\u0081\3\2\2\2\3")
        buf.write("\u0083\3\2\2\2\5\u0088\3\2\2\2\7\u0090\3\2\2\2\t\u0095")
        buf.write("\3\2\2\2\13\u009b\3\2\2\2\r\u00a1\3\2\2\2\17\u00a7\3\2")
        buf.write("\2\2\21\u00ae\3\2\2\2\23\u00b2\3\2\2\2\25\u00ba\3\2\2")
        buf.write("\2\27\u00be\3\2\2\2\31\u00c5\3\2\2\2\33\u00ce\3\2\2\2")
        buf.write("\35\u00d1\3\2\2\2\37\u00da\3\2\2\2!\u00dd\3\2\2\2#\u00e2")
        buf.write("\3\2\2\2%\u00e5\3\2\2\2\'\u00eb\3\2\2\2)\u00f3\3\2\2\2")
        buf.write("+\u00f5\3\2\2\2-\u00f7\3\2\2\2/\u00f9\3\2\2\2\61\u00fb")
        buf.write("\3\2\2\2\63\u00fd\3\2\2\2\65\u00ff\3\2\2\2\67\u0102\3")
        buf.write("\2\2\29\u0105\3\2\2\2;\u0108\3\2\2\2=\u010b\3\2\2\2?\u010d")
        buf.write("\3\2\2\2A\u0110\3\2\2\2C\u0112\3\2\2\2E\u0115\3\2\2\2")
        buf.write("G\u0118\3\2\2\2I\u011a\3\2\2\2K\u011c\3\2\2\2M\u011e\3")
        buf.write("\2\2\2O\u0120\3\2\2\2Q\u0122\3\2\2\2S\u0124\3\2\2\2U\u0126")
        buf.write("\3\2\2\2W\u0128\3\2\2\2Y\u012a\3\2\2\2[\u012c\3\2\2\2")
        buf.write("]\u012e\3\2\2\2_\u0139\3\2\2\2a\u0149\3\2\2\2c\u014b\3")
        buf.write("\2\2\2e\u0150\3\2\2\2g\u0156\3\2\2\2i\u015d\3\2\2\2k\u016e")
        buf.write("\3\2\2\2m\u0183\3\2\2\2o\u0185\3\2\2\2q\u018b\3\2\2\2")
        buf.write("s\u0194\3\2\2\2u\u01a2\3\2\2\2w\u01a4\3\2\2\2y\u01a8\3")
        buf.write("\2\2\2{\u01ae\3\2\2\2}\u01b7\3\2\2\2\177\u01c1\3\2\2\2")
        buf.write("\u0081\u01c4\3\2\2\2\u0083\u0084\7c\2\2\u0084\u0085\7")
        buf.write("w\2\2\u0085\u0086\7v\2\2\u0086\u0087\7q\2\2\u0087\4\3")
        buf.write("\2\2\2\u0088\u0089\7k\2\2\u0089\u008a\7p\2\2\u008a\u008b")
        buf.write("\7v\2\2\u008b\u008c\7g\2\2\u008c\u008d\7i\2\2\u008d\u008e")
        buf.write("\7g\2\2\u008e\u008f\7t\2\2\u008f\6\3\2\2\2\u0090\u0091")
        buf.write("\7x\2\2\u0091\u0092\7q\2\2\u0092\u0093\7k\2\2\u0093\u0094")
        buf.write("\7f\2\2\u0094\b\3\2\2\2\u0095\u0096\7c\2\2\u0096\u0097")
        buf.write("\7t\2\2\u0097\u0098\7t\2\2\u0098\u0099\7c\2\2\u0099\u009a")
        buf.write("\7{\2\2\u009a\n\3\2\2\2\u009b\u009c\7d\2\2\u009c\u009d")
        buf.write("\7t\2\2\u009d\u009e\7g\2\2\u009e\u009f\7c\2\2\u009f\u00a0")
        buf.write("\7m\2\2\u00a0\f\3\2\2\2\u00a1\u00a2\7h\2\2\u00a2\u00a3")
        buf.write("\7n\2\2\u00a3\u00a4\7q\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6")
        buf.write("\7v\2\2\u00a6\16\3\2\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9")
        buf.write("\7g\2\2\u00a9\u00aa\7v\2\2\u00aa\u00ab\7w\2\2\u00ab\u00ac")
        buf.write("\7t\2\2\u00ac\u00ad\7p\2\2\u00ad\20\3\2\2\2\u00ae\u00af")
        buf.write("\7q\2\2\u00af\u00b0\7w\2\2\u00b0\u00b1\7v\2\2\u00b1\22")
        buf.write("\3\2\2\2\u00b2\u00b3\7d\2\2\u00b3\u00b4\7q\2\2\u00b4\u00b5")
        buf.write("\7q\2\2\u00b5\u00b6\7n\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8")
        buf.write("\7c\2\2\u00b8\u00b9\7p\2\2\u00b9\24\3\2\2\2\u00ba\u00bb")
        buf.write("\7h\2\2\u00bb\u00bc\7q\2\2\u00bc\u00bd\7t\2\2\u00bd\26")
        buf.write("\3\2\2\2\u00be\u00bf\7u\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1")
        buf.write("\7t\2\2\u00c1\u00c2\7k\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4")
        buf.write("\7i\2\2\u00c4\30\3\2\2\2\u00c5\u00c6\7e\2\2\u00c6\u00c7")
        buf.write("\7q\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca")
        buf.write("\7k\2\2\u00ca\u00cb\7p\2\2\u00cb\u00cc\7w\2\2\u00cc\u00cd")
        buf.write("\7g\2\2\u00cd\32\3\2\2\2\u00ce\u00cf\7f\2\2\u00cf\u00d0")
        buf.write("\7q\2\2\u00d0\34\3\2\2\2\u00d1\u00d2\7h\2\2\u00d2\u00d3")
        buf.write("\7w\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5\7e\2\2\u00d5\u00d6")
        buf.write("\7v\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9")
        buf.write("\7p\2\2\u00d9\36\3\2\2\2\u00da\u00db\7q\2\2\u00db\u00dc")
        buf.write("\7h\2\2\u00dc \3\2\2\2\u00dd\u00de\7g\2\2\u00de\u00df")
        buf.write("\7n\2\2\u00df\u00e0\7u\2\2\u00e0\u00e1\7g\2\2\u00e1\"")
        buf.write("\3\2\2\2\u00e2\u00e3\7k\2\2\u00e3\u00e4\7h\2\2\u00e4$")
        buf.write("\3\2\2\2\u00e5\u00e6\7y\2\2\u00e6\u00e7\7j\2\2\u00e7\u00e8")
        buf.write("\7k\2\2\u00e8\u00e9\7n\2\2\u00e9\u00ea\7g\2\2\u00ea&\3")
        buf.write("\2\2\2\u00eb\u00ec\7k\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee")
        buf.write("\7j\2\2\u00ee\u00ef\7g\2\2\u00ef\u00f0\7t\2\2\u00f0\u00f1")
        buf.write("\7k\2\2\u00f1\u00f2\7v\2\2\u00f2(\3\2\2\2\u00f3\u00f4")
        buf.write("\t\2\2\2\u00f4*\3\2\2\2\u00f5\u00f6\t\3\2\2\u00f6,\3\2")
        buf.write("\2\2\u00f7\u00f8\t\4\2\2\u00f8.\3\2\2\2\u00f9\u00fa\t")
        buf.write("\5\2\2\u00fa\60\3\2\2\2\u00fb\u00fc\t\6\2\2\u00fc\62\3")
        buf.write("\2\2\2\u00fd\u00fe\t\7\2\2\u00fe\64\3\2\2\2\u00ff\u0100")
        buf.write("\7(\2\2\u0100\u0101\7(\2\2\u0101\66\3\2\2\2\u0102\u0103")
        buf.write("\7~\2\2\u0103\u0104\7~\2\2\u01048\3\2\2\2\u0105\u0106")
        buf.write("\7?\2\2\u0106\u0107\7?\2\2\u0107:\3\2\2\2\u0108\u0109")
        buf.write("\7#\2\2\u0109\u010a\7?\2\2\u010a<\3\2\2\2\u010b\u010c")
        buf.write("\7>\2\2\u010c>\3\2\2\2\u010d\u010e\7>\2\2\u010e\u010f")
        buf.write("\7?\2\2\u010f@\3\2\2\2\u0110\u0111\7@\2\2\u0111B\3\2\2")
        buf.write("\2\u0112\u0113\7@\2\2\u0113\u0114\7?\2\2\u0114D\3\2\2")
        buf.write("\2\u0115\u0116\7<\2\2\u0116\u0117\7<\2\2\u0117F\3\2\2")
        buf.write("\2\u0118\u0119\7*\2\2\u0119H\3\2\2\2\u011a\u011b\7+\2")
        buf.write("\2\u011bJ\3\2\2\2\u011c\u011d\7]\2\2\u011dL\3\2\2\2\u011e")
        buf.write("\u011f\7_\2\2\u011fN\3\2\2\2\u0120\u0121\7\60\2\2\u0121")
        buf.write("P\3\2\2\2\u0122\u0123\7.\2\2\u0123R\3\2\2\2\u0124\u0125")
        buf.write("\7=\2\2\u0125T\3\2\2\2\u0126\u0127\7<\2\2\u0127V\3\2\2")
        buf.write("\2\u0128\u0129\7}\2\2\u0129X\3\2\2\2\u012a\u012b\7\177")
        buf.write("\2\2\u012bZ\3\2\2\2\u012c\u012d\7?\2\2\u012d\\\3\2\2\2")
        buf.write("\u012e\u012f\7\61\2\2\u012f\u0130\7\61\2\2\u0130\u0134")
        buf.write("\3\2\2\2\u0131\u0133\n\b\2\2\u0132\u0131\3\2\2\2\u0133")
        buf.write("\u0136\3\2\2\2\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2")
        buf.write("\u0135\u0137\3\2\2\2\u0136\u0134\3\2\2\2\u0137\u0138\b")
        buf.write("/\2\2\u0138^\3\2\2\2\u0139\u013a\7\61\2\2\u013a\u013b")
        buf.write("\7,\2\2\u013b\u013f\3\2\2\2\u013c\u013e\13\2\2\2\u013d")
        buf.write("\u013c\3\2\2\2\u013e\u0141\3\2\2\2\u013f\u0140\3\2\2\2")
        buf.write("\u013f\u013d\3\2\2\2\u0140\u0142\3\2\2\2\u0141\u013f\3")
        buf.write("\2\2\2\u0142\u0143\7,\2\2\u0143\u0144\7\61\2\2\u0144\u0145")
        buf.write("\3\2\2\2\u0145\u0146\b\60\2\2\u0146`\3\2\2\2\u0147\u014a")
        buf.write("\5c\62\2\u0148\u014a\5e\63\2\u0149\u0147\3\2\2\2\u0149")
        buf.write("\u0148\3\2\2\2\u014ab\3\2\2\2\u014b\u014c\7v\2\2\u014c")
        buf.write("\u014d\7t\2\2\u014d\u014e\7w\2\2\u014e\u014f\7g\2\2\u014f")
        buf.write("d\3\2\2\2\u0150\u0151\7h\2\2\u0151\u0152\7c\2\2\u0152")
        buf.write("\u0153\7n\2\2\u0153\u0154\7u\2\2\u0154\u0155\7g\2\2\u0155")
        buf.write("f\3\2\2\2\u0156\u015a\t\t\2\2\u0157\u0159\t\n\2\2\u0158")
        buf.write("\u0157\3\2\2\2\u0159\u015c\3\2\2\2\u015a\u0158\3\2\2\2")
        buf.write("\u015a\u015b\3\2\2\2\u015bh\3\2\2\2\u015c\u015a\3\2\2")
        buf.write("\2\u015d\u015e\5m\67\2\u015e\u015f\b\65\3\2\u015fj\3\2")
        buf.write("\2\2\u0160\u0161\5m\67\2\u0161\u0163\5o8\2\u0162\u0164")
        buf.write("\5q9\2\u0163\u0162\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165")
        buf.write("\3\2\2\2\u0165\u0166\b\66\4\2\u0166\u016f\3\2\2\2\u0167")
        buf.write("\u016a\5m\67\2\u0168\u016a\5o8\2\u0169\u0167\3\2\2\2\u0169")
        buf.write("\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016c\5q9\2\u016c")
        buf.write("\u016d\b\66\5\2\u016d\u016f\3\2\2\2\u016e\u0160\3\2\2")
        buf.write("\2\u016e\u0169\3\2\2\2\u016fl\3\2\2\2\u0170\u0184\7\62")
        buf.write("\2\2\u0171\u0175\t\13\2\2\u0172\u0174\t\f\2\2\u0173\u0172")
        buf.write("\3\2\2\2\u0174\u0177\3\2\2\2\u0175\u0173\3\2\2\2\u0175")
        buf.write("\u0176\3\2\2\2\u0176\u0180\3\2\2\2\u0177\u0175\3\2\2\2")
        buf.write("\u0178\u017a\7a\2\2\u0179\u017b\t\f\2\2\u017a\u0179\3")
        buf.write("\2\2\2\u017b\u017c\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d")
        buf.write("\3\2\2\2\u017d\u017f\3\2\2\2\u017e\u0178\3\2\2\2\u017f")
        buf.write("\u0182\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2")
        buf.write("\u0181\u0184\3\2\2\2\u0182\u0180\3\2\2\2\u0183\u0170\3")
        buf.write("\2\2\2\u0183\u0171\3\2\2\2\u0184n\3\2\2\2\u0185\u0187")
        buf.write("\5O(\2\u0186\u0188\t\f\2\2\u0187\u0186\3\2\2\2\u0188\u0189")
        buf.write("\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a")
        buf.write("p\3\2\2\2\u018b\u018d\t\r\2\2\u018c\u018e\t\16\2\2\u018d")
        buf.write("\u018c\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u0190\3\2\2\2")
        buf.write("\u018f\u0191\t\f\2\2\u0190\u018f\3\2\2\2\u0191\u0192\3")
        buf.write("\2\2\2\u0192\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193r")
        buf.write("\3\2\2\2\u0194\u0198\7$\2\2\u0195\u0197\5u;\2\u0196\u0195")
        buf.write("\3\2\2\2\u0197\u019a\3\2\2\2\u0198\u0196\3\2\2\2\u0198")
        buf.write("\u0199\3\2\2\2\u0199\u019b\3\2\2\2\u019a\u0198\3\2\2\2")
        buf.write("\u019b\u019c\7$\2\2\u019c\u019d\b:\6\2\u019dt\3\2\2\2")
        buf.write("\u019e\u01a3\5w<\2\u019f\u01a0\7^\2\2\u01a0\u01a3\7$\2")
        buf.write("\2\u01a1\u01a3\n\17\2\2\u01a2\u019e\3\2\2\2\u01a2\u019f")
        buf.write("\3\2\2\2\u01a2\u01a1\3\2\2\2\u01a3v\3\2\2\2\u01a4\u01a5")
        buf.write("\7^\2\2\u01a5\u01a6\t\20\2\2\u01a6x\3\2\2\2\u01a7\u01a9")
        buf.write("\t\21\2\2\u01a8\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa")
        buf.write("\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ac\3\2\2\2")
        buf.write("\u01ac\u01ad\b=\2\2\u01adz\3\2\2\2\u01ae\u01b2\7$\2\2")
        buf.write("\u01af\u01b1\5u;\2\u01b0\u01af\3\2\2\2\u01b1\u01b4\3\2")
        buf.write("\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b5")
        buf.write("\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5\u01b6\b>\7\2\u01b6")
        buf.write("|\3\2\2\2\u01b7\u01bb\7$\2\2\u01b8\u01ba\5u;\2\u01b9\u01b8")
        buf.write("\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb")
        buf.write("\u01bc\3\2\2\2\u01bc\u01be\3\2\2\2\u01bd\u01bb\3\2\2\2")
        buf.write("\u01be\u01bf\5\177@\2\u01bf\u01c0\b?\b\2\u01c0~\3\2\2")
        buf.write("\2\u01c1\u01c2\7^\2\2\u01c2\u01c3\n\20\2\2\u01c3\u0080")
        buf.write("\3\2\2\2\u01c4\u01c5\13\2\2\2\u01c5\u01c6\bA\t\2\u01c6")
        buf.write("\u0082\3\2\2\2\26\2\u0134\u013f\u0149\u015a\u0163\u0169")
        buf.write("\u016e\u0175\u017c\u0180\u0183\u0189\u018d\u0192\u0198")
        buf.write("\u01a2\u01aa\u01b2\u01bb\n\b\2\2\3\65\2\3\66\3\3\66\4")
        buf.write("\3:\5\3>\6\3?\7\3A\b")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    INTEGER = 2
    VOID = 3
    ARRAY = 4
    BREAK = 5
    FLOAT = 6
    RETURN = 7
    OUT = 8
    BOOLEAN = 9
    FOR = 10
    STRING = 11
    CONTINUE = 12
    DO = 13
    FUNCTION = 14
    OF = 15
    ELSE = 16
    IF = 17
    WHILE = 18
    INHERIT = 19
    PLUS = 20
    MINUS = 21
    MUL = 22
    DIV = 23
    MOD = 24
    NOT = 25
    AND = 26
    OR = 27
    EQUAL = 28
    NOTEQUAL = 29
    LESS = 30
    LESSEQUAL = 31
    GREATER = 32
    GREATEREQUAL = 33
    DBCOLON = 34
    LROUNDBR = 35
    RROUNDBR = 36
    LSQUAREBR = 37
    RSQUAREBR = 38
    DOT = 39
    COMMA = 40
    SEMI_COLON = 41
    COLON = 42
    LBRACES = 43
    RBRACES = 44
    ASSIGN = 45
    CPP_CMT = 46
    C_CMT = 47
    BOOLEANLIT = 48
    TRUE = 49
    FALSE = 50
    IDENTIFIERS = 51
    INTLIT = 52
    FLOATLIT = 53
    STRINGLIT = 54
    WS = 55
    UNCLOSE_STRING = 56
    ILLEGAL_ESCAPE = 57
    ERROR_CHAR = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'integer'", "'void'", "'array'", "'break'", "'float'", 
            "'return'", "'out'", "'boolean'", "'for'", "'string'", "'continue'", 
            "'do'", "'function'", "'of'", "'else'", "'if'", "'while'", "'inherit'", 
            "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'::'", "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", 
            "'{'", "'}'", "'='", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "INTEGER", "VOID", "ARRAY", "BREAK", "FLOAT", "RETURN", 
            "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", 
            "OF", "ELSE", "IF", "WHILE", "INHERIT", "PLUS", "MINUS", "MUL", 
            "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "NOTEQUAL", "LESS", 
            "LESSEQUAL", "GREATER", "GREATEREQUAL", "DBCOLON", "LROUNDBR", 
            "RROUNDBR", "LSQUAREBR", "RSQUAREBR", "DOT", "COMMA", "SEMI_COLON", 
            "COLON", "LBRACES", "RBRACES", "ASSIGN", "CPP_CMT", "C_CMT", 
            "BOOLEANLIT", "TRUE", "FALSE", "IDENTIFIERS", "INTLIT", "FLOATLIT", 
            "STRINGLIT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "AUTO", "INTEGER", "VOID", "ARRAY", "BREAK", "FLOAT", 
                  "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", 
                  "DO", "FUNCTION", "OF", "ELSE", "IF", "WHILE", "INHERIT", 
                  "PLUS", "MINUS", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                  "EQUAL", "NOTEQUAL", "LESS", "LESSEQUAL", "GREATER", "GREATEREQUAL", 
                  "DBCOLON", "LROUNDBR", "RROUNDBR", "LSQUAREBR", "RSQUAREBR", 
                  "DOT", "COMMA", "SEMI_COLON", "COLON", "LBRACES", "RBRACES", 
                  "ASSIGN", "CPP_CMT", "C_CMT", "BOOLEANLIT", "TRUE", "FALSE", 
                  "IDENTIFIERS", "INTLIT", "FLOATLIT", "POSITIVE", "DECIMAl", 
                  "EXPONENT", "STRINGLIT", "STR_CHAR", "ESC_SEQ", "WS", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ILLESC", "ERROR_CHAR" ]

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
            actions[51] = self.INTLIT_action 
            actions[52] = self.FLOATLIT_action 
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
     


