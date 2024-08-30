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
.var 1 is y F from Label0 to Label1
	ldc 10.5
	fstore_1
	bipush 10
	iconst_5
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label5:
	fload_1
	ldc 2.5
	fsub
	fstore_1
Label6:
	goto Label7
Label4:
Label8:
	fload_1
	ldc 2.5
	fadd
	fstore_1
Label9:
Label7:
Label1:
	return
.limit stack 4
.limit locals 2
.end method
