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

.method public static pow(II)I
.var 0 is base I from Label0 to Label1
.var 1 is exp I from Label0 to Label1
Label0:
	iload_1
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_1
	ireturn
	goto Label5
Label4:
	iload_0
	iload_0
	iload_1
	iconst_1
	isub
	invokestatic MT22Class/pow(II)I
	imul
	ireturn
Label5:
Label1:
	ireturn
.limit stack 6
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is result I from Label0 to Label1
	iconst_2
	bipush 10
	invokestatic MT22Class/pow(II)I
	istore_1
Label1:
	return
.limit stack 2
.limit locals 2
.end method
