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
.var 1 is a F from Label0 to Label1
	ldc 2.5
	fstore_1
.var 2 is b F from Label0 to Label1
	fload_1
	ldc 2.0
	fmul
	fstore_2
Label1:
	return
.limit stack 2
.limit locals 3
.end method
