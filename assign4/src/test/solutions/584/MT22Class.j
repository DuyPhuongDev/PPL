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
.var 1 is s Ljava/lang/String; from Label0 to Label1
	ldc "abc"
	astore_1
.var 2 is t Ljava/lang/String; from Label0 to Label1
	aload_1
	ldc "def"
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore_2
Label1:
	return
.limit stack 2
.limit locals 3
.end method
