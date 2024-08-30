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

.method public static rootFunc()V
Label0:
	ldc 3.14
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 1
.limit locals 0
.end method

.method public static squareFunc()V
Label0:
	invokestatic MT22Class/rootFunc()V
	ldc 9.0
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MT22Class/squareFunc()V
Label1:
	return
.limit stack 0
.limit locals 1
.end method
