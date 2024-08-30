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

.method public static isEven(I)Z
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_2
	irem
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ireturn
Label1:
.limit stack 3
.limit locals 1
.end method

.method public static isOdd(I)Z
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_2
	irem
	iconst_0
	if_icmpeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ireturn
Label1:
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is evenResult Z from Label0 to Label1
.var 2 is oddResult Z from Label0 to Label1
	iconst_4
	invokestatic MT22Class/isEven(I)Z
	istore_1
	bipush 7
	invokestatic MT22Class/isOdd(I)Z
	istore_2
Label1:
	return
.limit stack 1
.limit locals 3
.end method
