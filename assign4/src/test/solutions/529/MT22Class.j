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
.var 1 is z I from Label0 to Label1
	iconst_0
	istore_1
Label4:
Label5:
	iload_1
	iconst_1
	iadd
	istore_1
Label6:
Label2:
	iload_1
	iconst_3
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label3
	goto Label4
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
.end method
