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
.var 1 is arr [[I from Label0 to Label1
	iconst_3
	anewarray [I
	dup
	iconst_0
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_3
	iastore
	dup
	iconst_1
	iconst_4
	iastore
	aastore
	dup
	iconst_2
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_5
	iastore
	dup
	iconst_1
	bipush 6
	iastore
	aastore
	astore_1
.var 2 is sum I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is i I from Label0 to Label1
.var 4 is j I from Label0 to Label1
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
	iconst_0
	istore 4
Label9:
	iload 4
	iconst_2
	if_icmpge Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label10
Label14:
	iload_2
	aload_1
	iload_3
	aaload
	iload 4
	iaload
	iadd
	istore_2
Label15:
Label13:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label9
Label10:
Label8:
Label13:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label2
Label3:
Label1:
	return
.limit stack 7
.limit locals 5
.end method
