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

.method public static sumArray([II)I
.var 0 is arr [I from Label0 to Label1
.var 1 is n I from Label0 to Label1
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
	aload_0
	iconst_0
	iaload
	ireturn
	goto Label5
Label4:
	aload_0
	iload_1
	iaload
	aload_0
	iload_1
	iconst_1
	isub
	invokestatic MT22Class/sumArray([II)I
	iadd
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
.var 1 is arr [I from Label0 to Label1
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	astore_1
.var 2 is total I from Label0 to Label1
	aload_1
	iconst_4
	invokestatic MT22Class/sumArray([II)I
	istore_2
Label1:
	return
.limit stack 4
.limit locals 3
.end method
