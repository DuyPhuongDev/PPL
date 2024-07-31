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
        self.typ = returnTyp
        self.inherit = inherit

class GlobalFunc(Symbol):
    def __init__(self, name: str, param: List[ParamSymbol], returnTyp: Type) -> None:
        self.name = name
        self.params = param
        self.typ = returnTyp

class GetPrototype(Visitor):
    def __init__(self, ast) -> None:
        self.ast = ast
    def visitProgram(self, ast, param):
        env = []
        for decl in ast.decls:
            self.visit(decl, env)
        return env
    
    def visitVarDecl(self, ast, param):
        param += [VarSymbol(ast.name, ast.typ)]
    
    def visitFuncDecl(self, ast, param):
        params = reduce(lambda prev, curr: self.visit(curr, prev), ast.params, [])
        param += [FuncSymbol(ast.name, params , ast.return_type, ast.inherit)]
    
    def visitParamDecl(self, ast, param):
        param += [ParamSymbol(ast.name, ast.typ, ast.inherit, ast.out)]
        return param
     
class InferType():
    @staticmethod
    def infer(name, typ, param):
        for env in param:
            found = Utils().lookup(name, env,lambda x: x.name)
            if found:
                found.typ = typ
                return typ
               
class StaticChecker(Visitor):
    
    def check(self):
        return self.visitProgram(self.ast, [])

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
            GlobalFunc("preventDefault", [], VoidType())
        ]]
        self.curr_var = None #luu bien hien tai dang visit
        self.prototype = [] # luu moi truong so bo cua chuong trinh
        self.curr_func = None # luu name cua function hien tai dang duoc vieng tham
        self.inloop = []
        self.returned = False
    
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
        #ltype = l.typ if type(ast.left) is Id else l 
        rtype = self.visit(ast.right, param)
        #rtype = r.typ if type(ast.right) is Id else r
        if type(ltype) is AutoType:
            if type(rtype) is AutoType: raise TypeMismatchInExpression(ast)
            else: ltype = InferType.infer(ast.left.name,rtype,param)
        else:
            if type(rtype) is AutoType: rtype = InferType.infer(ast.right.name, ltype, param)
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
        #etype = e.typ if type(ast.val) is Id else e
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
        #print('visit Id')
        ##print([list(map(lambda x: (x.name, type(x)), i)) for i in param])
        if self.curr_var is not None and self.curr_var == ast.name:
            raise Undeclared(Identifier(), ast.name)
        found = None
        for env in param:
            sym = Utils().lookup(ast.name, env, lambda x: x.name)
            if sym is not None and type(sym) in [VarSymbol, ParamSymbol]:
                found = sym
                break
        if found is None:
            raise Undeclared(Identifier(), ast.name)
        return found.typ
        
    def visitArrayCell(self, ast, param): 
        #print("visit arraycell")
        found = None
        for env in param:
            found = Utils().lookup(ast.name, env, lambda x: x.name)
            if found: break
        if not found: raise Undeclared(Identifier(), ast.name)
        if type(found.typ) is not ArrayType: raise TypeMismatchInExpression(ast)
        # dimension must be integer
        dimentyps = [self.visit(x, param) for x in ast.cell]
        #print(dimentyps)
        for typ in dimentyps:
            if type(typ) is not IntegerType: raise TypeMismatchInExpression(ast)
        if len(found.typ.dimensions)<len(dimentyps): raise TypeMismatchInExpression(ast)
        return found.typ.typ
            
    def visitIntegerLit(self, ast, param): return IntegerType()
    def visitFloatLit(self, ast, param): return FloatType()
    def visitStringLit(self, ast, param): return StringType()
    def visitBooleanLit(self, ast, param): return BooleanType()
    
    def visitArrayLit(self, ast, param):
        #print("visit arraylit")
        exprs = [self.visit(x, param) for x in ast.explist]
        #print(exprs)
        # get first element to typ of array
        first = exprs[0] if len(exprs) else None
        if not first: return AutoType()
        for i in range(1,len(exprs)):
            if type(exprs[i]) is not type(first): raise IllegalArrayLiteral(ast)
            if type(first) is ArrayType:
                # check dimen + typ of element
                if first.dimensions != exprs[i].dimensions: raise IllegalArrayLiteral(ast)
        if type(first) is ArrayType:
            #print(ArrayType([len(exprs)] + first.dimensions, first.typ))
            return ArrayType([len(exprs)] + first.dimensions, first.typ)
        
        #print(ArrayType([len(exprs)], first))
        return ArrayType([len(exprs)], first)
        
    
    def visitFuncCall(self, ast, param):
        #print("visit funcCall")
        func = Utils().lookup(ast.name if ast.name != 'super' else self.curr_func.inherit, self.prototype, lambda x: x.name) 
        #print(func.name)
        if not func: raise Undeclared(Function(), ast.name)
        if type(func.typ) is VoidType: raise TypeMismatchInExpression(ast)
        args = [self.visit(x, param) for x in ast.args]
        if(len(func.params) != len(args)): raise TypeMismatchInExpression(ast)
            # check type
        for i in range(len(args)):
            if type(func.params[i].typ) is AutoType:
                func.params[i].typ = args[i]
            if type(func.params[i].typ) is not type(args[i]): raise TypeMismatchInExpression(ast)
        return func.typ

    ##### Statements #####
    def visitAssignStmt(self, ast, param):
        #print('visit assignStmt')
        #print("current function:", self.curr_func.name)
        lhs = self.visit(ast.lhs, param)
        rhs = self.visit(ast.rhs, param)
        
        if type(lhs) is ArrayType: raise TypeMismatchInStatement(ast)
        if type(lhs) is AutoType:
            if type(rhs) is AutoType: raise TypeMismatchInStatement(ast)
            lhs = InferType.infer(ast.lhs.name, rhs, param)
        if type(lhs) in [ArrayType, VoidType]:
            raise TypeMismatchInStatement(ast)
        if type(rhs) is AutoType:
            found = Utils().lookup(ast.rhs.name, self.prototype, lambda x: x.name)
            found.typ = lhs
            rhs = found.typ
            #print(found.typ)
        if type(lhs) != type(rhs): raise TypeMismatchInStatement(ast)
        ##print(list(map(lambda x: (x.name, x.typ), param[1])))
        return lhs # tra ve type cua lhs  
        
    def visitBlockStmt(self, ast, param):
        #print("visit blockstmt")
        # tao moi truong local cho new scope
        #local = [[]] + param
        ##print(list(map(lambda x: x.name, param[-1])))
        # check blockscope cua function => true: xu ly super, preventDefautl
        func = param[1][-1]
        #print(func.name, 'is function' if type(func) is FuncSymbol else 'is not function')
        #print(list(map(lambda x: x.name, param[0])))
        if type(func) is FuncSymbol and func.inherit != None:
            parent = Utils().lookup(func.inherit, list(filter(lambda x: type(x) is FuncSymbol, self.prototype)),lambda x: x.name)
            if parent is None: raise Undeclared(Function(), func.inherit)
            first = ast.body[0] if len(ast.body) != 0 else None # first stmt in body of function
            if not first or type(first) != CallStmt or first.name not in ['super', 'preventDefault']:
                # call super()
                if len(parent.params) != 0: raise InvalidStatementInFunction(func.name)
            
        for stmt in ast.body:
            #print(stmt)
            local = [[]] + param if  type(stmt) is BlockStmt else param
            if self.returned and type(stmt) is ReturnStmt: continue
            self.visit(stmt, local)

    def visitIfStmt(self, ast, param):
        #print("visit ifstmt")
        # output cua expr cond must be boolean
        cond = self.visit(ast.cond, param)
        if type(cond) is not BooleanType: raise TypeMismatchInStatement(ast)
        # tao scope cho if stmt
        local = [[]] + param
        self.visit(ast.tstmt, local)
        if ast.fstmt: self.visit(ast.stmt, local)
        
    def visitForStmt(self, ast, param):
        #print("visit for stmt")
        self.inloop += ['for']
        local = [[]] + param
        local[0] += [VarSymbol(ast.init.lhs.name,AutoType())]
        init = self.visit(ast.init, local)
        if type(init) is not IntegerType: raise TypeMismatchInStatement(ast)
        cond = self.visit(ast.cond, local)
        if type(cond) is not BooleanType: raise TypeMismatchInStatement(ast)
        updt = self.visit(ast.upd, local)
        if type(updt) is not IntegerType: raise TypeMismatchInStatement(ast)
        #print(list(map(lambda x: x.name, local[0])))
        self.visit(ast.stmt, local)
        self.inloop.pop(-1)
    def visitWhileStmt(self, ast, param): 
        #print("visit While stmt")
        self.inloop.append('while')
        if type(self.visit(ast.cond, param)) is not BooleanType: raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt, param)
        self.inloop.pop(-1)
    def visitDoWhileStmt(self, ast, param): 
        #print("visit do-while stmt")
        self.inloop.append("do-while")
        self.visit(ast.stmt, param)
        if type(self.visit(ast.cond, param)) is not BooleanType: raise TypeMismatchInStatement(ast)
        self.inloop.pop(-1)
    def visitBreakStmt(self, ast, param):
        #print("break")
        if(self.inloop == []): raise MustInLoop(ast)
    def visitContinueStmt(self, ast, param):
        #print("continue")
        if(self.inloop == []): raise MustInLoop(ast)
    def visitReturnStmt(self, ast, param):
        print("return stmt")
        self.returned = True
        found = Utils().lookup(self.curr_func.name,self.prototype, lambda x: x.name)
        if not ast.expr:
            if type(self.curr_func.typ) is AutoType: found.typ = VoidType()
            elif type(self.curr_func.typ) is not VoidType: raise TypeMismatchInStatement(ast)
        else:
            infertyp = self.visit(ast.expr, param)
            if type(self.curr_func.typ) is AutoType:
                if type(infertyp) in [AutoType, VoidType]: raise TypeMismatchInStatement(ast)
                else: found.typ = infertyp        
            if type(self.curr_func.typ) is VoidType: raise TypeMismatchInStatement(ast)
            if type(self.curr_func.typ) is not type(infertyp): raise TypeMismatchInStatement(ast)
        
    def visitCallStmt(self, ast, param): 
        #print("visit callstmt")
        # check callfunc is declared
        # with super
        # get list pram of funccall, callstmt
        args = [self.visit(x, param) for x in ast.args]
        if ast.name == 'super':
            parentF = Utils().lookup(self.curr_func.inherit, self.prototype, lambda x: x.name)
            if len(args) < len(parentF.params): raise TypeMismatchInExpression(None)
            if len(args) > len(parentF.params): raise TypeMismatchInExpression(ast.args[len(parentF.params)])              
            for i in range(len(args)):
                if type(parentF.params[i].typ) is AutoType:
                    parentF.params[i].typ = args[i]
                #print(type(args[i]), '-', type(parentF.params[i].typ))
                if type(args[i]) != type(parentF.params[i].typ): raise TypeMismatchInExpression(ast.args[i])
            
        else:
            callfunc = Utils().lookup(ast.name, param[-1], lambda x: x.name)
            if callfunc is None:
                callfunc = Utils().lookup(ast.name, self.prototype, lambda x: x.name)
                if callfunc is None or type(callfunc) is not FuncSymbol: raise Undeclared(FuncSymbol(), ast.name)
            else: 
                if type(callfunc) not in [FuncSymbol, GlobalFunc]: raise Undeclared(Function(), ast.name)
            
            
            #print(args)
            #print(callfunc.params)
            # check length cua 2 func
            if(len(callfunc.params) != len(args)): raise TypeMismatchInStatement(ast)
            # check type
            for i in range(len(args)):
                if type(callfunc.params[i].typ) is AutoType:
                    callfunc.params[i].typ = args[i]
                if type(callfunc.params[i].typ) is not type(args[i]): raise TypeMismatchInStatement(ast)
            
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
        # check xem co redeclare
        # param[-1]: global scope
        funcsym = Utils().lookup(ast.name,param[-1], lambda x: x.name)
        if funcsym != None: raise Redeclared(Function(), ast.name)
        # get list param
        params = [] # luu parameter cua func con
        
        if ast.inherit != None:
            # co ke thua => tim func cha
            ##print(list(map(lambda x: x.name,filter(lambda x: type(x) is FuncSymbol, self.prototype))))
            parentFunc = Utils().lookup(ast.inherit, list(filter(lambda x: type(x) is FuncSymbol, self.prototype)), lambda x: x.name)
            if parentFunc is None: raise Undeclared(Function(), ast.inherit)
            # tim thay ham cha trong global scope => get paramdecl has inherit keyword
            for x in parentFunc.params:
                if x.inherit: params += [x]
        
        idxInherit = len(params) # luu so luong param dc inherit tu ham cha
        
        for x in ast.params:
            params = self.visit(x, params)
        local_param = params[idxInherit:]
        #func = FuncSymbol(ast.name, local_param, ast.return_type, ast.inherit)
        func = Utils().lookup(ast.name, self.prototype, lambda x: x.name)
        param[-1] += [func]
        # get all param cua func cha dua vao local
        local = [params] + param # scope cua ham
        # vieng tham body
        self.curr_func = func
        self.visit(ast.body, local)
        self.curr_func = None
        self.returned = False

    ##### Program #####
    def visitProgram(self, ast, param):
        # first get prototype 
        self.prototype = GetPrototype(self.ast).visit(self.ast, param)
        print(list(map(lambda x: x.name if type(x) is VarSymbol or type(x) is GlobalFunc else f'func {x.typ} {x.name}({list(map(lambda y: (y.name, y.typ), x.params))})', self.prototype)))
        for decl in ast.decls:
            self.visit(decl,self.env)
        
        print(list(map(lambda x: x.name if type(x) is VarSymbol or type(x) is GlobalFunc else f'func {x.typ} {x.name}({list(map(lambda y: (y.name, y.typ), x.params))})', self.env[0])))
        ismain = False
        #print(list(map(lambda x: x.name, param[0])))
        for func in self.env[0]:
            if type(func) is FuncSymbol and func.name == 'main' and type(func.typ) is VoidType and func.params == []:
                ismain = True
                break
        
        if not ismain: raise NoEntryPoint() 