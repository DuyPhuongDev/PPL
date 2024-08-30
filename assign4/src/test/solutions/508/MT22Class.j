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
.var 1 is x Z from Label0 to Label1
	iconst_1
	istore_1
.var 2 is y Z from Label0 to Label1
	iconst_0
	istore_2
.var 3 is z Z from Label0 to Label1
	iload_1
	iload_2
	ior
	istore_3
Label1:
	return
.limit stack 4
.limit locals 4
.end method
