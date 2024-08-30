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
.var 1 is x I from Label0 to Label1
	iconst_5
	istore_1
	iload_1
	bipush 10
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label5:
	iload_1
	iconst_1
	iadd
	istore_1
Label6:
	goto Label7
Label4:
Label8:
.var 2 is y I from Label8 to Label9
	bipush 20
	istore_2
	iload_2
	iconst_1
	iadd
	istore_2
Label9:
Label7:
Label1:
	return
.limit stack 4
.limit locals 3
.end method
