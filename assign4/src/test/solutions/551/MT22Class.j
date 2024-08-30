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

.method public static fibonacci(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_0
	ireturn
	goto Label5
Label4:
	iload_0
	iconst_1
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	iconst_1
	ireturn
	goto Label9
Label8:
	iload_0
	iconst_1
	isub
	invokestatic MT22Class/fibonacci(I)I
	iload_0
	iconst_2
	isub
	invokestatic MT22Class/fibonacci(I)I
	iadd
	ireturn
Label9:
Label5:
Label1:
	ireturn
.limit stack 7
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is fib I from Label0 to Label1
	bipush 7
	invokestatic MT22Class/fibonacci(I)I
	istore_1
Label1:
	return
.limit stack 1
.limit locals 2
.end method
