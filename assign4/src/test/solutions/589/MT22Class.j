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
.var 1 is arr [Ljava/lang/String; from Label0 to Label1
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "hello"
	aastore
	dup
	iconst_1
	ldc "world"
	aastore
	astore_1
.var 2 is concat Ljava/lang/String; from Label0 to Label1
	ldc ""
	astore_2
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
Label2:
	iload_3
	iconst_2
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label7:
	aload_2
	aload_1
	iload_3
	aaload
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore_2
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
