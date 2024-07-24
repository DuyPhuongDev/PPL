from AST import *
from Visitor import Visitor
from StaticError import *
from Utils import *
from abc import ABC
from functools import reduce

class Symbol: pass
class VarSymbol(Symbol):
    def __init__(self, name: str, typ: Type):
        self.name = name
        self.typ = typ

class ParamSymbol(Symbol):
    def __init__(self,name: str, typ: Type, inherit: bool = False, out: bool = False ) -> None:
        self.name = name
        self.typ = typ
        self.inherit = inherit
        self.out = out
        
class FuncSymbol(Symbol):
    def __init__(self,name: str, params: List[ParamSymbol], returnTyp: Type, inherit: str or None) -> None:
        self.name = name
        self.params = params
        self.type = returnTyp
        self.inherit = inherit

class GlobalFunc(Symbol):
    def __init__(self, name: str, param: List[ParamSymbol], returnTyp: Type) -> None:
        self.name = name
        self.param = param
        self.typ = returnTyp

class GetPrototype(Visitor):
    def visitProgram(self, ast, param):
        for decl in ast.decls:
            self.visit(decl, param)
    
    def visitVarDecl(self, ast, param):
        param += [VarSymbol(ast.name, ast.typ)]
    
    def visitFuncDecl(self, ast, param):
        params = reduce(lambda prev, curr: self.visit(curr, prev), ast.params, [])
        param += [FuncSymbol(ast.name, params , ast.return_type, ast.inherit)]
    
    def visitParamDecl(self, ast, param):
        param += [ParamSymbol(ast.name, ast.typ, ast.inherit, ast.out)]
        return param
        
class StaticChecker(Visitor):
    
    def check(self):
        return self.visitProgram(self.ast, self.env)

    def __init__(self, ast):
        self.ast = ast
        self.env = [[
            GlobalFunc("readInteger", [], IntegerType()),
            GlobalFunc("printInteger", [ParamSymbol("", IntegerType())], VoidType()),
            GlobalFunc("readFloat", [], FloatType()),
            GlobalFunc("writeFloat", [ParamSymbol("", FloatType())], VoidType()),
            GlobalFunc("readBoolean", [], BooleanType()),
            GlobalFunc("printboolean", [ParamSymbol("", BooleanType())], VoidType()),
            GlobalFunc("readString", [], StringType()),
            GlobalFunc("printString", [ParamSymbol("", StringType())], VoidType()),
            GlobalFunc("super", [], VoidType()),
            GlobalFunc("preventDefault", [], VoidType()),
        ]]
        self.curr_var = None #luu bien hien tai dang visit
        self.prototype = [] # luu moi truong so bo cua chuong trinh
    
    # type
    def visitIntegerType(self, ast, param): return IntegerType()
    def visitFloatType(self, ast, param): return FloatType()
    def visitBooleanType(self, ast, param): return BooleanType()
    def visitStringType(self, ast, param): return StringType()
    def visitArrayType(self, ast, param): return ArrayType(ast.dimensions, ast.typ)
    def visitAutoType(self, ast, param): return AutoType()
    def visitVoidType(self, ast, param): return VoidType()

    ######  Expr  #####
    def visitBinExpr(self, ast, param):
        ltype = self.visit(ast.left, param)
        rtype = self.visit(ast.right, param)
        if ast.op in ['-', '+', '*', '/']:
            if type(ltype) is IntegerType and type(rtype) is IntegerType:
                return IntegerType() if ast.op != '/' else FloatType()
            if (type(ltype),type(rtype)) in [(IntegerType, FloatType), (FloatType, IntegerType), (FloatType, FloatType)]:
                return FloatType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op == '%': 
            if type(ltype) is IntegerType and type(rtype) is IntegerType:
                return IntegerType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['&&', '||']:
            if type(ltype) is BooleanType and type(rtype) is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op == '::':
            if type(ltype) is StringType and type(rtype) is StringType:
                return StringType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['==', '!=']:
            if (type(ltype), type(rtype)) in [(IntegerType, IntegerType), (IntegerType, BooleanType), (BooleanType, IntegerType), (BooleanType, BooleanType)]:
                return BooleanType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['<', '>', '<=', '>=']:
            if (type(ltype), type(rtype)) in [(IntegerType, IntegerType), (IntegerType, FloatType), (FloatType, IntegerType), (FloatType,FloatType)]:
                return BooleanType()
            raise TypeMismatchInExpression(ast)
            
    def visitUnExpr(self, ast, param):
        etype = self.visit(ast.val, param)
        if ast.op == '-':
            if type(etype) in [IntegerType, FloatType]:
                return etype
            raise TypeMismatchInExpression(ast)
        if ast.op == '!':
            if type(etype) is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ast)
        
    def visitId(self, ast, param):
        # return type of id if not found => undeclared
        """ bien dang khai bao kh dc sd x: integer = x + 3; => error """
        if self.curr_var is not None and self.curr_var == ast.name:
            raise Undeclared(Identifier(), ast.name)
        found = None
        for syms in param:
            sym = Utils().lookup(ast.name, syms, lambda x: x.name)
            if sym is not None and type(sym) is VarDecl:
                isfound = sym
                break
        if found is None:
            raise Undeclared(Identifier(), ast.name)
        return found.typ
        
    def visitArrayCell(self, ast, param): pass
    def visitIntegerLit(self, ast, param): return IntegerType()
    def visitFloatLit(self, ast, param): return FloatType()
    def visitStringLit(self, ast, param): return StringType()
    def visitBooleanLit(self, ast, param): return BooleanType()
    def visitArrayLit(self, ast, param): pass
    def visitFuncCall(self, ast, param): pass

    ##### Statements #####
    def visitAssignStmt(self, ast, param):
        lhs = self.visit(ast.lhs, param)
        rhs = self.visit(ast.rhs, param)
        if type(lhs) in [ArrayType, VoidType]:
            raise TypeMismatchInStatement(ast)
        if type(lhs) != type(rhs): raise TypeMismatchInStatement(ast)
    def visitBlockStmt(self, ast, param):
        # tao moi truong local cho new scope
        local = [[]] + param
        # check blockscope cua function => true: xu ly super, preventDefautl
        func = param[-1][-1]
        if type(func) is FuncSymbol and func.inherit != None:
            parent = Utils().lookup(func.inherit, list(filter(lambda x: type(x) is FuncSymbol, self.prototype)),lambda x: x.name)
            if parent is None: raise Undeclared(Function(), func.inherit)
            first = ast.body[0] if len(ast.body) != 0 else None # first stmt in body of function
            if not first or type(first) != CallStmt:
                # call super()
                if len(parent.params) != 0: raise InvalidStatementInFunction(func.name)
            if first.name not in ['super', 'preventDefault']: raise InvalidStatementInFunction(func.name)
        
        for stmt in ast.body:
            self.visit(stmt, local)
            

    def visitIfStmt(self, ast, param): pass
    def visitForStmt(self, ast, param): pass
    def visitWhileStmt(self, ast, param): pass
    def visitDoWhileStmt(self, ast, param): pass
    def visitBreakStmt(self, ast, param): pass
    def visitContinueStmt(self, ast, param): pass
    def visitReturnStmt(self, ast, param): pass
    def visitCallStmt(self, ast, param): pass

    ##### Declared #####
    def visitVarDecl(self, ast, param):
        if Utils().lookup(ast.name, param[0], lambda x: x.name) is not None:
            raise Redeclared(Variable(), ast.name) 
        self.curr_var = ast.name
        # full declared
        if ast.init is not None:
            rhstype = self.visit(ast.init, param) # lay type cua rhs
            if type(ast.typ) is AutoType and type(rhstype) is AutoType: raise Invalid(Variable(), ast.name)
            # handle with auto type => infer type
            if type(rhstype) in [BooleanType, IntegerType, FloatType, StringType, ArrayType]:
                if type(ast.typ) is AutoType or (type(ast.typ) == type(rhstype)):
                    param[0] += [VarSymbol(ast.name, rhstype)]
                else: raise TypeMismatchInVarDecl(ast)
            elif type(ast.typ) in [BooleanType, IntegerType, FloatType, StringType, ArrayType] and type(rhstype) is AutoType:
                # tim kiem func symbol rhs trong symbol table
                for syms in param:
                    found = Utils().lookup(ast.name, syms, lambda x: x.name)
                    found.typ = ast.typ #can quay lai than ham check lai -> skip now
                    break     
            else: raise TypeMismatchInVarDecl(ast)
        
        if ast.init is None:
            if type(ast.typ) is AutoType: raise Invalid(Variable(), ast.name)
            elif type(ast.typ) in [BooleanType, IntegerType, FloatType, StringType, ArrayType]:
                param[0] += [VarSymbol(ast.name, ast.typ)]
            else: raise TypeMismatchInVarDecl(ast)
            self.curr_var = None
                
    def visitParamDecl(self, ast, param):
        paramSym = Utils().lookup(ast.name,param,lambda x: x.name)
        if paramSym != None: raise Redeclared(Parameter(), ast.name)
        param += [ParamSymbol(ast.name,ast.typ, ast.inherit, ast.out)]
        return param
    def visitFuncDecl(self, ast, param): 
        # xu ly inhertit => skip now
        # check xem co redeclare
        # param[-1]: global scope
        funcsym = Utils().lookup(ast.name,param[-1], lambda x: x.name)
        if funcsym != None: raise Redeclared(Function(), ast.name)
        # get list param
        params = [] # luu parameter cua func con
        
        if ast.inherit != None:
            # co ke thua => tim func cha
            #print(list(map(lambda x: x.name,filter(lambda x: type(x) is FuncSymbol, self.prototype))))
            parentFunc = Utils().lookup(ast.inherit, list(filter(lambda x: type(x) is FuncSymbol, self.prototype)), lambda x: x.name)
            if parentFunc is None: raise Undeclared(Function(), ast.inherit)
            # tim thay ham cha trong global scope => get paramdecl has inherit keyword
            for x in parentFunc.params:
                if x.inherit: params += [x]
        
        idxInherit = len(params) # luu so luong param dc inherit tu ham cha
        
        for x in ast.params:
            params = self.visit(x, params)
        local_param = params[idxInherit:]
        func = FuncSymbol(ast.name, local_param, ast.return_type, ast.inherit)
        param[-1] += [func]
        # get all param cua func cha dua vao local
        local = [params] + param # scope cua ham
        # vieng tham body
        self.visit(ast.body, local)

    ##### Program #####
    def visitProgram(self, ast, param):
        # first get prototype 
        GetPrototype().visit(ast, self.prototype)
        print(list(map(lambda x: x.name if type(x) is VarSymbol or type(x) is GlobalFunc else f'func {x.name}({list(map(lambda y: (y.name, y.typ), x.params))})', self.prototype)))
        
        for decl in ast.decls:
            self.visit(decl,param)
        ismain = False
        #print(list(map(lambda x: x.name, param[0])))
        for func in param[0]:
            if type(func) is FuncSymbol and func.name == 'main' and type(func.type) is VoidType and func.params == []:
                ismain = True
                break
        
        if not ismain: raise NoEntryPoint() 