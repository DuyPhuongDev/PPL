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

.method public static concat(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
.var 0 is s1 Ljava/lang/String; from Label0 to Label1
.var 1 is s2 Ljava/lang/String; from Label0 to Label1
Label0:
	aload_0
	aload_1
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	areturn
Label1:
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is result Ljava/lang/String; from Label0 to Label1
	ldc "Hello"
	ldc "World"
	invokestatic MT22Class/concat(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
	astore_1
Label1:
	return
.limit stack 2
.limit locals 2
.end method
