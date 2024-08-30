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

.method public static sum(III)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c I from Label0 to Label1
Label0:
	iload_0
	iload_1
	iadd
	iload_2
	iadd
	ireturn
Label1:
.limit stack 2
.limit locals 3
.end method

.method public static product(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	iload_1
	imul
	ireturn
Label1:
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is result I from Label0 to Label1
	iconst_1
	iconst_2
	iconst_3
	invokestatic MT22Class/product(II)I
	iconst_4
	invokestatic MT22Class/sum(III)I
	istore_1
Label1:
	return
.limit stack 3
.limit locals 2
.end method
