.source MT22Class.java
.class public MT22Class
.super java/lang/Object

.method public <init>()V
.var 0 is this LMT22Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a I from Label2 to Label3
	bipush 10
	istore_1
Label4:
.var 2 is b I from Label4 to Label5
	bipush 20
	istore_2
	iload_1
	iload_2
	iadd
	istore_1
Label5:
Label3:
Label1:
	return
.limit stack 2
.limit locals 3
.end method
