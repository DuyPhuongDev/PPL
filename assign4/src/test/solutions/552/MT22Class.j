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

.method public static gcd(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
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
	iload_0
	ireturn
	goto Label5
Label4:
	iload_1
	iload_0
	iload_1
	irem
	invokestatic MT22Class/gcd(II)I
	ireturn
Label5:
Label1:
	ireturn
.limit stack 5
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is res I from Label0 to Label1
	bipush 48
	bipush 18
	invokestatic MT22Class/gcd(II)I
	istore_1
Label1:
	return
.limit stack 2
.limit locals 2
.end method
