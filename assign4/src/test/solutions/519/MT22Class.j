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
	ldc "Hello"
	astore_1
	iconst_1
	ifle Label2
Label3:
	aload_1
	ldc " World"
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore_1
Label4:
Label2:
Label1:
	return
.limit stack 3
.limit locals 2
.end method
