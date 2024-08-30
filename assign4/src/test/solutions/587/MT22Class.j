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
.var 1 is arr [F from Label0 to Label1
	iconst_3
	newarray float
	dup
	iconst_0
	ldc 1.1
	fastore
	dup
	iconst_1
	ldc 2.2
	fastore
	dup
	iconst_2
	ldc 3.3
	fastore
	astore_1
.var 2 is product F from Label0 to Label1
	ldc 1.0
	fstore_2
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
Label2:
	iload_3
	iconst_3
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label7:
	fload_2
	aload_1
	iload_3
	faload
	fmul
	fstore_2
Label8:
Label6:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label2
Label3:
Label1:
	return
.limit stack 5
.limit locals 4
.end method
